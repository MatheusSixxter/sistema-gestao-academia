import re

from django.core.exceptions import ValidationError


def validate_cnpj(value):
    """
    Valida CNPJ numérico ou alfanumérico,
    incluindo os dois dígitos verificadores.
    """

    cnpj = re.sub(r'[./\-\s]', '', str(value)).upper()

    # CNPJ possui 14 posições:
    # 12 alfanuméricas + 2 numéricas.
    if not re.fullmatch(r'[A-Z0-9]{12}\d{2}', cnpj):
        raise ValidationError(
            'Informe um CNPJ válido com 14 caracteres.'
        )

    # Impede sequências inválidas com os 12 primeiros
    # caracteres iguais.
    if len(set(cnpj[:12])) == 1:
        raise ValidationError(
            'Informe um CNPJ válido.'
        )

    def calculate_digit(base):
        if len(base) == 12:
            weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        else:
            weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        total = sum(
            (ord(character) - 48) * weight
            for character, weight in zip(base, weights)
        )

        remainder = total % 11

        return '0' if remainder < 2 else str(11 - remainder)

    first_digit = calculate_digit(cnpj[:12])

    second_digit = calculate_digit(
        cnpj[:12] + first_digit
    )

    calculated_digits = first_digit + second_digit

    if cnpj[-2:] != calculated_digits:
        raise ValidationError(
            'Os dígitos verificadores do CNPJ são inválidos.'
        )
