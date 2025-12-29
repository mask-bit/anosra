# Anosra Backend - API REST

Backend completo do sistema Anosra desenvolvido em Python + Flask + PostgreSQL.

## Estrutura do Projeto

```
backend/
├── app/
│   ├── __init__.py          # Inicialização do Flask
│   ├── config.py            # Configurações
│   ├── models/              # Modelos de dados (SQLAlchemy)
│   │   ├── user.py
│   │   ├── business.py
│   │   ├── expense.py
│   │   └── employee.py
│   ├── routes/              # Rotas da API
│   │   ├── auth.py
│   │   ├── business.py
│   │   ├── expense.py
│   │   ├── employee.py
│   │   ├── reports.py
│   │   └── integration.py
│   └── services/            # Lógica de negócio
│       ├── auth_service.py
│       ├── business_service.py
│       ├── expense_service.py
│       ├── report_service.py
│       └── open_finance_service.py
├── run.py                   # Arquivo principal
├── requirements.txt         # Dependências
└── .env.example            # Variáveis de ambiente
```

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Configure o banco de dados PostgreSQL:
```bash
# Crie o banco de dados
createdb anosra

# Execute as migrações
flask db upgrade
```

6. Execute o servidor:
```bash
python run.py
```

## Endpoints da API

### Autenticação
- `POST /api/auth/register` - Cadastro de usuário
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Dados do usuário atual (requer token)

### Negócios
- `POST /api/business/` - Criar negócio
- `GET /api/business/` - Listar negócios
- `GET /api/business/<id>` - Buscar negócio
- `PUT /api/business/<id>` - Atualizar negócio
- `DELETE /api/business/<id>` - Excluir negócio

### Despesas
- `POST /api/expenses/` - Criar despesa
- `GET /api/expenses/business/<id>` - Listar despesas
- `GET /api/expenses/business/<id>/summary` - Resumo de despesas
- `PUT /api/expenses/<id>` - Atualizar despesa
- `DELETE /api/expenses/<id>` - Excluir despesa

### Funcionários
- `POST /api/employees/` - Criar funcionário
- `GET /api/employees/business/<id>` - Listar funcionários
- `GET /api/employees/business/<id>/analysis` - Análise de folha
- `PUT /api/employees/<id>` - Atualizar funcionário
- `DELETE /api/employees/<id>` - Excluir funcionário

### Relatórios
- `GET /api/reports/financial/<id>` - Relatório financeiro
- `GET /api/reports/employees/<id>` - Relatório de funcionários
- `GET /api/reports/business/<id>` - Relatório do negócio
- `GET /api/reports/inconsistencies/<id>` - Detecção de inconsistências
- `GET /api/reports/comparative/<id>` - Relatório comparativo

### Integração
- `POST /api/integration/open-finance/connect` - Conectar Open Finance
- `POST /api/integration/open-finance/disconnect/<id>` - Desconectar
- `POST /api/integration/open-finance/sync/<id>` - Sincronizar transações
- `GET /api/integration/open-finance/status/<id>` - Status da conexão

## Tecnologias

- **Flask** - Framework web
- **SQLAlchemy** - ORM
- **PostgreSQL** - Banco de dados
- **JWT** - Autenticação
- **bcrypt** - Hash de senhas
- **Flask-CORS** - CORS

## Segurança

- Senhas hasheadas com bcrypt
- Autenticação via JWT
- CORS configurado
- Validação de permissões em todas as rotas

## Notas

- O serviço Open Finance está simulado para desenvolvimento
- Em produção, integrar com APIs reais dos bancos
- Configure corretamente as variáveis de ambiente em produção
