# SGE — Sistema de Gestão de Estoque

Sistema web de gestão de estoque desenvolvido em **Django**, com controle de produtos, marcas, categorias, fornecedores, entradas e saídas de mercadoria, dashboard com indicadores e um agente de inteligência artificial (SGE Agent) que analisa os dados do estoque.

## 🧰 Stack

| Tecnologia | Uso |
|---|---|
| Python 3.13 | Linguagem |
| Django 6.1 | Framework web (templates + ORM) |
| Django REST Framework | API REST |
| Simple JWT | Autenticação da API via tokens JWT |
| PostgreSQL 15 | Banco de dados (via Docker Compose) |
| SQLite | Banco de dados para execução local (padrão) |
| OpenAI API | Agente de análise de estoque (SGE Agent) |
| Bootstrap + Bootstrap Icons | Interface |
| uv | Gerenciamento de dependências |
| Docker / Docker Compose | Contêineres da aplicação e do banco |

## ✨ Funcionalidades

- **Autenticação** — login/logout de usuários, com controle de acesso por permissões em todas as telas.
- **Dashboard** — visão geral com gráficos de produtos por marca e por categoria, produtos em estoque e fora de estoque.
- **Marcas, Categorias e Fornecedores** — CRUD completo (listar, criar, detalhar, editar e excluir) com busca.
- **Produtos** — cadastro com título, categoria, marca, fornecedor, descrição, número de série, preço de custo e preço de venda.
- **Entradas (Inflows)** — registro de entrada de produtos no estoque.
- **Saídas (Outflows)** — registro de saída de produtos do estoque.
- **API REST** — endpoints versionados em `/api/v1/` autenticados por JWT.
- **SGE Agent (IA)** — análise do estoque em linguagem natural usando a API da OpenAI, exibida no dashboard e disponível via comando de gerenciamento.

## 📁 Estrutura do projeto

```
sge/
├── app/            # Configurações, templates base, static (CSS) e home/dashboard
├── authentication/ # App de autenticação (usuários e JWT)
├── brands/         # Marcas
├── categories/     # Categorias
├── suppliers/      # Fornecedores
├── products/       # Produtos
├── inflows/        # Entradas de estoque
├── outflows/       # Saídas de estoque
├── ai/             # SGE Agent (OpenAI), prompts e comando de gerenciamento
├── services/       # Serviços auxiliares
├── docker-compose.yml
├── Dockerfile
└── pyproject.toml
```

Cada app de domínio segue o mesmo padrão: `models.py`, `forms.py`, `views.py`, `urls.py`, `serializers.py`, `admin.py` e `templates/`.

## 🚀 Como executar

### Com Docker (recomendado)

1. Crie um arquivo `.env` na raiz com pelo menos:

   ```env
   USE_POSTGRES=1
   POSTGRES_DB=sge
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_HOST=sge_db
   POSTGRES_PORT=5432
   OPENAI_API_KEY=sua-chave-openai   # opcional: habilita o SGE Agent
   OPENAI_MODEL=gpt-5.4-mini
   ```

2. Suba os contêineres:

   ```bash
   docker compose up --build
   ```

   A aplicação sobe em **http://localhost:8000** (migrations aplicadas automaticamente). O Postgres fica em `localhost:5432` com dados persistidos no volume `postgres_data`.

### Localmente (sem Docker)

```bash
uv sync                 # instala as dependências
uv run python manage.py migrate
uv run python manage.py runserver
```

Sem `USE_POSTGRES=1`, o projeto usa **SQLite** (`db.sqlite3`) por padrão.

### Criar superusuário

```bash
uv run python manage.py createsuperuser
```

Acesse o admin Django em **http://localhost:8000/admin/**.

## 🔐 API REST

A API usa autenticação **JWT** (access token válido por 1 dia, refresh por 7 dias) e permissões por modelo (`DjangoModelPermissions`).

### Autenticação

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/api/v1/authentication/token/` | Obtém access e refresh tokens |
| POST | `/api/v1/authentication/token/refresh/` | Renova o access token |
| POST | `/api/v1/authentication/token/verify/` | Verifica validade do token |

```bash
# obter token
curl -X POST http://localhost:8000/api/v1/authentication/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "seu_usuario", "password": "sua_senha"}'

# consumir endpoint protegido
curl http://localhost:8000/api/v1/products/ \
  -H "Authorization: Bearer <seu_access_token>"
```

### Recursos

| Método | Endpoint | Descrição |
|---|---|---|
| GET / POST | `/api/v1/brands/` | Lista / cria marcas |
| GET / PUT / PATCH / DELETE | `/api/v1/brands/<id>/` | Detalhe / atualiza / exclui marca |
| GET / POST | `/api/v1/categories/` | Lista / cria categorias |
| GET / PUT / PATCH / DELETE | `/api/v1/categories/<id>/` | Detalhe / atualiza / exclui categoria |
| GET / POST | `/api/v1/suppliers/` | Lista / cria fornecedores |
| GET / PUT / PATCH / DELETE | `/api/v1/suppliers/<id>/` | Detalhe / atualiza / exclui fornecedor |
| GET / POST | `/api/v1/products/` | Lista / cria produtos |
| GET / PUT / PATCH / DELETE | `/api/v1/products/<id>/` | Detalhe / atualiza / exclui produto |
| GET / POST | `/api/v1/inflows/` | Lista / cria entradas |
| GET | `/api/v1/inflows/<id>/` | Detalhe de entrada |
| GET / POST | `/api/v1/outflows/` | Lista / cria saídas |
| GET | `/api/v1/outflows/<id>/` | Detalhe de saída |

## 🤖 SGE Agent

O agente envia os dados de produtos e saídas para a OpenAI e retorna uma análise do estoque (exibida no dashboard em Markdown).

- Defina `OPENAI_API_KEY` (e opcionalmente `OPENAI_MODEL`) no `.env`.
- Também é possível invocá-lo por linha de comando:

  ```bash
  uv run python manage.py sge_agent_invoke
  ```

## 🖥️ Telas do sistema

Todas as telas de CRUD seguem o padrão de rotas do app de categorias (o mesmo vale para brands, suppliers, products, inflows e outflows):

```
/<recurso>/list/       # listagem com busca e paginação (10 por página)
/<recurso>/create/     # criação
/<recurso>/<id>/detail # detalhamento
/<recurso>/<id>/update # edição
/<recurso>/<id>/delete # exclusão
```

> Ex.: `/categories/list/`, `/products/create/`, `/inflows/list/`, etc.

## 📝 Licença

Projeto de estudo — sem licença definida.
