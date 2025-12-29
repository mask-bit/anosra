# Guia de Instalação - Sistema Anosra

## Requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação Rápida

### 1. Instalar Dependências
```bash
cd backend
pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente
O arquivo `.env` já está configurado com valores padrão para desenvolvimento.

### 3. Iniciar o Servidor
```bash
python run.py
```

O servidor iniciará em: **http://localhost:5000**

## Páginas Disponíveis

- `/` - Landing page
- `/login` - Login
- `/cadastro` - Cadastro de usuário
- `/dashboard` - Dashboard principal
- `/negocios` - Gestão de negócios
- `/despesas` - Controle de despesas
- `/funcionarios` - Gestão de funcionários
- `/relatorios` - Relatórios inteligentes
- `/integracao` - Integração Open Finance
- `/configuracoes` - Configurações do sistema

## API Endpoints

Todas as rotas da API estão em `/api/`:

### Autenticação
- `POST /api/auth/register` - Cadastro
- `POST /api/auth/login` - Login
- `POST /api/auth/recover-password` - Recuperar senha

### Negócios
- `POST /api/business/` - Criar negócio
- `GET /api/business/` - Listar negócios
- `GET /api/business/<id>` - Detalhes do negócio
- `PUT /api/business/<id>` - Atualizar negócio
- `GET /api/business/<id>/analytics` - Análises inteligentes

### Despesas
- `POST /api/expenses/` - Criar despesa
- `GET /api/expenses/` - Listar despesas
- `DELETE /api/expenses/<id>` - Deletar despesa

### Funcionários
- `POST /api/employees/` - Criar funcionário
- `GET /api/employees/` - Listar funcionários
- `PUT /api/employees/<id>` - Atualizar funcionário
- `DELETE /api/employees/<id>` - Deletar funcionário

### Relatórios
- `GET /api/reports/financial` - Relatório financeiro
- `GET /api/reports/comparative` - Relatório comparativo

### Integração
- `POST /api/integration/open-finance/connect` - Conectar Open Finance
- `GET /api/integration/open-finance/status` - Status da conexão
- `POST /api/integration/open-finance/sync` - Sincronizar dados

## Banco de Dados

Por padrão usa **SQLite** (arquivo `anosra.db`).

Para usar **PostgreSQL**:
1. Instale: `pip install psycopg2-binary`
2. Altere `DATABASE_URL` no `.env`:
   ```
   DATABASE_URL=postgresql://usuario:senha@localhost:5432/anosra
   ```

## Problemas Comuns

### Erro "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Erro de porta em uso
Altere a porta em `run.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Banco de dados não criado
O banco é criado automaticamente na primeira execução.
Para recriar: delete o arquivo `anosra.db` e rode novamente.

## Estrutura do Projeto

```
backend/
├── app/
│   ├── __init__.py          # Configuração Flask
│   ├── config.py            # Configurações
│   ├── models/              # Modelos do banco
│   ├── routes/              # Rotas da API
│   └── services/            # Lógica de negócio
├── database/                # Scripts de banco
├── .env                     # Variáveis de ambiente
├── requirements.txt         # Dependências
└── run.py                   # Iniciar servidor

frontend/
├── templates/               # Páginas HTML
└── static/
    ├── css/                # Estilos
    └── js/                 # JavaScript
```

## Desenvolvimento

O sistema está configurado com:
- Autenticação JWT
- CORS habilitado
- SQLAlchemy ORM
- Migrações com Flask-Migrate
- Análises inteligentes de negócio
- Integração Open Finance (simulada)

## Produção

Para deploy em produção:
1. Altere `FLASK_ENV=production` no `.env`
2. Configure chaves secretas fortes
3. Use PostgreSQL ou MySQL
4. Configure um servidor WSGI (Gunicorn, uWSGI)
5. Use um proxy reverso (Nginx, Apache)
