# 🏋️ SGA — Sistema de Gestão de Academia

<p align="center">
  <img src="https://img.shields.io/badge/Python-Backend-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-6.1.2-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/DRF-3.18.3-red?style=for-the-badge&logo=django&logoColor=white" alt="Django REST Framework">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SimpleJWT-5.5.1-black?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="SimpleJWT">
</p>

<p align="center">
  <strong>Sistema web para gerenciamento de academias, alunos, equipamentos, exercícios e fichas de treino.</strong>
</p>

<p align="center">
  <a href="https://github.com/MatheusSixxter/sistema-gestao-academia">Repositório</a> •
  <a href="#-sobre-o-projeto">Sobre</a> •
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-api-rest">API REST</a> •
  <a href="#-instalação-e-execução">Instalação</a>
</p>

---

## 📖 Sobre o projeto

O **SGA (Sistema de Gestão de Academia)** é uma aplicação web desenvolvida com Python e Django, voltada ao gerenciamento de operações e informações de uma academia.

O sistema permite centralizar o gerenciamento de alunos, equipamentos, exercícios, fornecedores e fichas de treino, oferecendo recursos para organizar as informações e acompanhar indicadores operacionais por meio de dashboards gerenciais.

A aplicação utiliza uma arquitetura modular, dividida em diferentes aplicações Django, com responsabilidades específicas para cada domínio do sistema.

Além da interface web, o projeto conta com uma **API REST desenvolvida com Django REST Framework**, disponibilizando operações para os principais módulos da aplicação, com autenticação JWT e controle de permissões.

### 🎯 Objetivos do projeto

- Desenvolver uma aplicação web completa para gerenciamento de academias.
- Implementar regras de negócio para gerenciamento de alunos e equipamentos.
- Desenvolver um sistema de fichas de treino personalizadas.
- Trabalhar com relacionamentos entre entidades utilizando Django ORM.
- Construir dashboards com métricas calculadas a partir dos dados do sistema.
- Desenvolver APIs REST para integração e comunicação com outros sistemas.
- Implementar autenticação JWT e controle de permissões.
- Utilizar PostgreSQL como banco de dados relacional.

---

## 🚀 Funcionalidades

### 👥 Gestão de alunos

- Cadastro, listagem, consulta, edição e exclusão de alunos.
- Armazenamento de informações pessoais e de contato.
- Validação de CPF.
- Gerenciamento de planos de matrícula.
- Controle de status dos alunos (ativo e inativo).
- Pesquisa de alunos por nome, CPF e telefone.
- Paginação dos resultados.

### 📋 Gestão de fichas de treino

- Criação de fichas de treino personalizadas.
- Associação de fichas aos respectivos alunos.
- Definição de datas de início e término.
- Controle de status das fichas (ativa e inativa).
- Gerenciamento dos exercícios vinculados a cada ficha.
- Organização dos exercícios por ordem de execução.

### 💪 Gestão de exercícios

- Cadastro, listagem, edição e exclusão de exercícios.
- Associação de exercícios aos equipamentos.
- Organização por categorias e grupos musculares.
- Descrição e identificação dos exercícios.
- Controle de disponibilidade dos exercícios.

### 📝 Exercícios personalizados nas fichas

Cada exercício vinculado a uma ficha possui configurações individuais:

- Exercício selecionado.
- Ordem de execução.
- Quantidade de séries.
- Número de repetições.
- Carga em quilogramas.
- Tempo de descanso em segundos.
- Observações personalizadas.

A estrutura permite adicionar diferentes exercícios a uma mesma ficha, mantendo as configurações específicas de cada um.

### 🏋️ Gestão de equipamentos

- Cadastro, listagem, consulta, edição e exclusão de equipamentos.
- Associação de equipamentos às respectivas marcas.
- Organização por categorias:
  - Máquinas.
  - Pesos livres.
  - Acessórios.
  - Cardio.
  - Outros.
- Controle de quantidade disponível.
- Classificação do estado de conservação:
  - Novo.
  - Excelente.
  - Bom.
  - Regular.
  - Ruim.
  - Danificado.
- Controle de equipamentos ativos e inativos.
- Filtros por nome, categoria, marca e condição.

### 🏷️ Gestão de marcas

- Cadastro e gerenciamento de marcas.
- Descrição das marcas.
- Controle de status ativo/inativo.
- Associação das marcas aos equipamentos.

### 🏭 Gestão de fornecedores

- Cadastro e gerenciamento de fornecedores.
- Armazenamento de CNPJ.
- Validação de CNPJ.
- Cadastro de telefone e e-mail.
- Associação dos fornecedores às entradas de equipamentos.

### 📥 Controle de entradas de equipamentos

- Registro de entradas de equipamentos.
- Associação da entrada ao equipamento correspondente.
- Identificação do fornecedor responsável.
- Registro da quantidade adquirida.
- Armazenamento do valor total da entrada.
- Registro da data da compra.
- Consulta e pesquisa do histórico de entradas.

### 📊 Dashboard gerencial

O sistema disponibiliza um dashboard com indicadores calculados a partir das informações armazenadas no banco de dados.

**Métricas de alunos:**

- Total de alunos cadastrados.
- Total de alunos ativos.
- Total de alunos inativos.
- Média de novos alunos nos últimos seis meses completos.

**Métricas gerais da academia:**

- Total de fichas de treino.
- Total de fornecedores cadastrados.
- Total de exercícios cadastrados.
- Quantidade total de equipamentos em estoque, considerando as quantidades registradas.

**Gráficos gerenciais:**

- Evolução dos cadastros de alunos ao longo dos meses.
- Distribuição dos equipamentos por categoria.

---

## 🔌 API REST

O projeto disponibiliza uma API REST desenvolvida com **Django REST Framework (DRF)**, permitindo o acesso aos recursos do sistema por meio de requisições HTTP.

A API contempla os principais módulos da aplicação, utilizando serializers para transformar os dados dos modelos Django em representações JSON.

### Recursos disponibilizados

| Recurso | Endpoint |
|---|---|
| Alunos | `/api/v1/athletes/` |
| Marcas | `/api/v1/brands/` |
| Equipamentos | `/api/v1/equipments/` |
| Exercícios | `/api/v1/exercises/` |
| Fornecedores | `/api/v1/suppliers/` |
| Entradas de equipamentos | `/api/v1/equipmentsentry/` |
| Fichas de treino | `/api/v1/workoutplan/` |
| Exercícios das fichas | `/api/v1/workoutplan/{workout_plan_id}/exercises/` |

### Operações HTTP

Os endpoints utilizam as classes genéricas do Django REST Framework para disponibilizar operações de consulta, criação, atualização e exclusão.

| Método HTTP | Operação |
|---|---|
| GET | Listar ou consultar registros |
| POST | Criar registros |
| PUT | Atualizar registros |
| PATCH | Atualizar parcialmente registros |
| DELETE | Excluir registros |

### Exemplos de endpoints

**Alunos:**

```http
GET    /api/v1/athletes/
POST   /api/v1/athletes/

GET    /api/v1/athletes/{id}/
PUT    /api/v1/athletes/{id}/
PATCH  /api/v1/athletes/{id}/
DELETE /api/v1/athletes/{id}/
```

**Equipamentos:**

```http
GET    /api/v1/equipments/
POST   /api/v1/equipments/

GET    /api/v1/equipments/{id}/
PUT    /api/v1/equipments/{id}/
PATCH  /api/v1/equipments/{id}/
DELETE /api/v1/equipments/{id}/
```

O mesmo padrão de operações é utilizado nos recursos de marcas, exercícios, fornecedores e entradas de equipamentos.

### 🏋️ API de fichas de treino

A API de fichas de treino possui uma estrutura específica para gerenciar os exercícios vinculados a cada ficha.

**Gerenciamento das fichas:**

```http
GET    /api/v1/workoutplan/
POST   /api/v1/workoutplan/

GET    /api/v1/workoutplan/{id}/
PUT    /api/v1/workoutplan/{id}/
PATCH  /api/v1/workoutplan/{id}/
DELETE /api/v1/workoutplan/{id}/
```

**Gerenciamento dos exercícios de uma ficha:**

```http
GET    /api/v1/workoutplan/{workout_plan_id}/exercises/
POST   /api/v1/workoutplan/{workout_plan_id}/exercises/

GET    /api/v1/workoutplan/{workout_plan_id}/exercises/{id}/
PUT    /api/v1/workoutplan/{workout_plan_id}/exercises/{id}/
PATCH  /api/v1/workoutplan/{workout_plan_id}/exercises/{id}/
DELETE /api/v1/workoutplan/{workout_plan_id}/exercises/{id}/
```

Essa organização permite gerenciar os exercícios dentro do contexto de cada ficha de treino, mantendo a relação entre as entidades.

---

## 🔐 Autenticação e controle de permissões

A API utiliza autenticação baseada em **JSON Web Token (JWT)**, implementada com a biblioteca SimpleJWT.

O Django REST Framework está configurado globalmente para utilizar JWT como mecanismo de autenticação e exigir autenticação e permissões de modelo nos endpoints.

### Mecanismos de segurança

- Autenticação JWT.
- Geração de Access Token e Refresh Token.
- Verificação de tokens.
- Proteção dos endpoints.
- Controle de acesso com `IsAuthenticated`.
- Controle de permissões de modelo com `DjangoModelPermissions`.

### Endpoints de autenticação

**Obter tokens:**

```http
POST /api/v1/authentication/token/
```

Exemplo de requisição:

```json
{
    "username": "seu_usuario",
    "password": "sua_senha"
}
```

**Atualizar Access Token:**

```http
POST /api/v1/authentication/token/refresh/
```

Exemplo:

```json
{
    "refresh": "SEU_REFRESH_TOKEN"
}
```

**Verificar token:**

```http
POST /api/v1/authentication/token/verify/
```

Exemplo:

```json
{
    "token": "SEU_ACCESS_TOKEN"
}
```

### Validade dos tokens

| Token | Validade |
|---|---|
| Access Token | 1 dia |
| Refresh Token | 7 dias |

### Autorização das requisições

Após obter o Access Token, envie-o no cabeçalho HTTP das requisições protegidas:

```http
Authorization: Bearer SEU_ACCESS_TOKEN
Content-Type: application/json
```

---

## 🛠️ Tecnologias e ferramentas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal do backend |
| Django 6.1.2 | Framework de desenvolvimento web |
| Django REST Framework 3.18.3 | Desenvolvimento da API REST |
| SimpleJWT 5.5.1 | Autenticação baseada em JWT |
| PostgreSQL | Banco de dados relacional |
| psycopg2 | Conexão com PostgreSQL |
| Django ORM | Mapeamento e manipulação de dados |
| Python Decouple | Gerenciamento de variáveis de ambiente |
| HTML5 | Estrutura das interfaces |
| CSS3 | Estilização das interfaces |
| Bootstrap 5 | Construção de interfaces responsivas |
| JavaScript | Interatividade e gráficos |
| Git | Controle de versão |
| GitHub | Hospedagem do código-fonte |
| Postman | Testes e validação da API |
| Flake8 7.5.0 | Análise estática e padronização do código |

---

## 🏗️ Arquitetura do projeto

O SGA utiliza uma arquitetura modular baseada nas aplicações do Django, separando as funcionalidades de acordo com suas responsabilidades.

### Estrutura de diretórios

```text
sistema-gestao-academia/
│
├── accounts/           # Cadastro e gerenciamento de usuários
│
├── app/                # Configurações principais do Django
│   ├── templates/      # Templates compartilhados
│   ├── settings.py     # Configurações do projeto
│   └── urls.py         # Roteamento principal
│
├── authentication/     # Autenticação e endpoints JWT
│
├── athletes/           # Gerenciamento de alunos
│
├── workouts/           # Fichas de treino e exercícios vinculados
│
├── exercises/          # Cadastro e gerenciamento de exercícios
│
├── brands/             # Gerenciamento de marcas
│
├── equipments/         # Gerenciamento de equipamentos
│
├── suppliers/          # Gerenciamento de fornecedores
│
├── equipmentsentry/    # Controle de entradas de equipamentos
│
├── dashboards/         # Indicadores e métricas gerenciais
│
├── .flake8             # Configurações do Flake8
├── .gitignore          # Arquivos ignorados pelo Git
├── manage.py           # Gerenciador de comandos Django
├── requirements.txt    # Dependências do projeto
└── requirements_dev.txt # Dependências de desenvolvimento
```

### Responsabilidade das aplicações

| Aplicação | Responsabilidade |
|---|---|
| `accounts` | Registro, login e logout de usuários |
| `app` | Configurações centrais, templates compartilhados e roteamento |
| `authentication` | Geração, atualização e verificação de tokens JWT |
| `athletes` | Cadastro e gerenciamento de alunos |
| `workouts` | Gerenciamento de fichas e exercícios vinculados |
| `exercises` | Cadastro e gerenciamento de exercícios |
| `brands` | Cadastro e gerenciamento de marcas |
| `equipments` | Gerenciamento de equipamentos |
| `suppliers` | Cadastro e gerenciamento de fornecedores |
| `equipmentsentry` | Registro de entradas de equipamentos |
| `dashboards` | Cálculo de métricas e apresentação de gráficos |

### Modelagem e relacionamentos

A aplicação utiliza relacionamentos entre os modelos Django para representar as entidades do sistema.

Entre os principais relacionamentos:

- Alunos possuem fichas de treino.
- Fichas de treino possuem exercícios vinculados.
- Exercícios podem estar associados a equipamentos.
- Equipamentos possuem marcas.
- Entradas de equipamentos estão relacionadas a equipamentos e fornecedores.

A modelagem de `WorkoutPlan` e `WorkoutExercise` permite organizar os exercícios individualmente, com configurações específicas para cada ficha de treino.

---

## ⚙️ Instalação e execução

Siga as instruções abaixo para executar o projeto localmente.

### Pré-requisitos

- Python compatível com as dependências do projeto.
- Git instalado.
- PostgreSQL instalado e configurado.
- Pip disponível.

### 1. Clone o repositório

```bash
git clone https://github.com/MatheusSixxter/sistema-gestao-academia.git
```

Entre no diretório:

```bash
cd sistema-gestao-academia
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

Para instalar as dependências de desenvolvimento:

```bash
pip install -r requirements_dev.txt
```

### 5. Configure as variáveis de ambiente

O projeto utiliza Python Decouple para carregar configurações sensíveis.

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_secreta

DB_NAME=nome_do_banco
DB_USER=usuario_postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

Configure os valores de acordo com seu ambiente PostgreSQL.

**Importante:** não compartilhe credenciais, senhas ou chaves secretas no repositório.

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Crie um superusuário

```bash
python manage.py createsuperuser
```

Siga as instruções do terminal para cadastrar o usuário administrativo.

### 8. Execute o servidor

```bash
python manage.py runserver
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Qualidade de código

O projeto utiliza Flake8 para análise estática e padronização do código Python.

As configurações estão centralizadas no arquivo `.flake8`.

Para executar a análise:

```bash
flake8 .
```

---

## 🔒 Segurança

O projeto utiliza recursos do Django e Django REST Framework para implementar autenticação e controle de acesso.

Entre os mecanismos utilizados:

- Autenticação de usuários.
- Proteção de páginas por autenticação.
- Controle de permissões nas operações da aplicação web.
- Autenticação JWT na API.
- Permissões de modelo com DjangoModelPermissions.
- Validação de senhas com os validadores nativos do Django.

Para utilização em produção, configure adequadamente `DEBUG`, `ALLOWED_HOSTS`, HTTPS, chaves secretas e credenciais do banco de dados.

---

## 🤝 Contribuição

Sugestões e contribuições são bem-vindas.

1. Faça um fork do projeto.
2. Crie uma branch para sua funcionalidade:

```bash
git checkout -b feature/nova-funcionalidade
```

3. Realize suas alterações.
4. Faça o commit:

```bash
git commit -m "feat: adiciona nova funcionalidade"
```

5. Envie suas alterações:

```bash
git push origin feature/nova-funcionalidade
```

6. Abra um Pull Request descrevendo as modificações realizadas.

---

## 📄 Licença

Este projeto ainda não possui uma licença de distribuição definida.

A utilização, modificação e redistribuição do código devem respeitar os direitos do autor até que uma licença seja formalmente definida.

---

## 👨‍💻 Desenvolvedor

**Matheus Andrade de Souza**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em desenvolvimento Backend utilizando Python e Django.

Interesses em desenvolvimento de aplicações web, APIs REST, modelagem de dados, regras de negócio e arquitetura de sistemas.

- **GitHub:** [MatheusSixxter](https://github.com/MatheusSixxter)
- **LinkedIn:** [Matheus Andrade](https://www.linkedin.com/in/matheus-andrade-de-souza-a31145423/)

---

<p align="center">
  Desenvolvido com Python, Django e dedicação. 🚀
</p>
