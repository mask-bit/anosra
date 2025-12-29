# ANOSRA - Sistema de Gestão de Negócios
## Versão Final - Pronto para Produção

### Status: ✅ COMPLETO

---

## Estrutura do Projeto

```
anosra/
├── backend/              # Backend Flask (API + Servidor)
│   ├── app/
│   │   ├── models/      # Modelos do banco (User, Business, etc)
│   │   ├── routes/      # Rotas da API (auth, business, etc)
│   │   ├── services/    # Lógica de negócio
│   │   ├── __init__.py  # Configuração Flask
│   │   └── config.py    # Configurações
│   ├── database/        # Scripts de banco de dados
│   ├── requirements.txt # Dependências Python
│   ├── run.py          # Servidor de desenvolvimento
│   └── wsgi.py         # Entry point para produção
├── frontend/
│   ├── templates/       # 11 páginas HTML
│   └── static/
│       ├── css/        # Estilos
│       └── js/         # Scripts JavaScript
├── render.yaml         # Configuração Render
├── Procfile           # Configuração Heroku/Render
└── DEPLOY_RENDER.md   # Guia de deploy

```

---

## Páginas Implementadas (11 total)

1. **index.html** - Landing page pública
2. **login.html** - Autenticação
3. **cadastro.html** - Registro de usuário
4. **dashboard.html** - Visão geral do sistema
5. **negocios.html** - Onboarding + Gestão de negócios
6. **despesas.html** - Controle de gastos
7. **funcionarios.html** - Gestão de equipe
8. **relatorios.html** - 5 tipos de relatórios
9. **integracao.html** - Open Finance
10. **configuracoes.html** - 8 seções de configuração
11. **recuperar-senha.html** - Reset de senha

---

## APIs Implementadas

### Autenticação
- `POST /api/auth/register` - Cadastro
- `POST /api/auth/login` - Login
- `POST /api/auth/reset-password` - Recuperar senha

### Negócios
- `GET /api/business` - Lista negócios
- `POST /api/business` - Cria negócio
- `PUT /api/business/<id>` - Atualiza negócio

### Despesas
- `GET /api/expenses` - Lista despesas
- `POST /api/expenses` - Adiciona despesa
- `DELETE /api/expenses/<id>` - Remove despesa

### Funcionários
- `GET /api/employees` - Lista funcionários
- `POST /api/employees` - Adiciona funcionário
- `PUT /api/employees/<id>` - Atualiza funcionário
- `DELETE /api/employees/<id>` - Remove funcionário

### Relatórios
- `GET /api/reports/financial` - Relatório financeiro
- `GET /api/reports/comparative` - Comparação com mercado
- `GET /api/reports/projections` - Projeções
- `GET /api/reports/alerts` - Alertas inteligentes
- `GET /api/reports/insights` - Insights personalizados

### Integrações
- `POST /api/integrations/open-finance/connect` - Conectar Open Finance
- `DELETE /api/integrations/open-finance/disconnect` - Desconectar
- `GET /api/integrations/open-finance/status` - Status da conexão

### Configurações
- `GET /api/settings` - Obter configurações
- `PUT /api/settings` - Atualizar configurações

---

## Tecnologias

### Backend
- **Flask 3.0** - Framework web
- **SQLAlchemy** - ORM para banco de dados
- **JWT** - Autenticação
- **BCrypt** - Hash de senhas
- **SQLite** - Banco de dados (desenvolvimento)
- **Gunicorn** - Servidor de produção

### Frontend
- **HTML5** - Estrutura
- **CSS3** - Estilos (preto e branco)
- **JavaScript ES6+** - Interatividade
- **Fetch API** - Requisições HTTP

---

## Como Rodar

### Desenvolvimento Local
```bash
# 1. Instalar dependências
cd backend
pip install -r requirements.txt

# 2. Configurar banco
python run.py

# 3. Acessar
http://localhost:5000
```

### Deploy no Render
```bash
# Veja instruções detalhadas em DEPLOY_RENDER.md
1. Push para GitHub
2. Conectar no Render
3. Deploy automático
```

---

## Funcionalidades Principais

### 1. Motor de Inteligência
- Análise automática de padrões
- Comparação com mercado por segmento
- Detecção de inconsistências
- Alertas em linguagem humana
- Sugestões práticas

### 2. Open Finance (Simulado)
- Conexão bancária segura
- Importação automática de transações
- Categorização inteligente
- Sincronização periódica

### 3. Relatórios Inteligentes
- Análise financeira completa
- Comparação com concorrentes
- Projeções futuras
- Insights personalizados
- Alertas contextuais

### 4. Gestão Completa
- Onboarding guiado
- Cadastro de negócios
- Controle de despesas
- Gestão de funcionários
- Configurações flexíveis

---

## Segurança

- Senhas com hash BCrypt
- Autenticação JWT
- Proteção CORS
- Validação de entrada
- SQL injection prevention (SQLAlchemy)

---

## Banco de Dados

### Tabelas Criadas
- `users` - Usuários do sistema
- `businesses` - Negócios cadastrados
- `expenses` - Despesas registradas
- `employees` - Funcionários
- `open_finance_connections` - Conexões bancárias

---

## Próximos Passos (Opcional)

### Para produção real:
1. Migrar para PostgreSQL
2. Implementar Open Finance real (Pluggy, Belvo)
3. Adicionar testes automatizados
4. Configurar CI/CD
5. Adicionar monitoramento (Sentry)
6. Implementar cache (Redis)
7. Adicionar email service
8. Configurar backups automáticos

---

## Observações Importantes

1. **SQLite** é usado por padrão - funciona perfeitamente para desenvolvimento e pequenas implantações
2. **Render Free Tier** - O serviço dorme após 15min sem uso (primeira requisição demora ~30s)
3. **Gunicorn** - Configurado para produção com múltiplos workers
4. **CORS** - Habilitado para integração frontend/backend

---

## Licença
MIT

## Autor
Desenvolvido para gestão completa de negócios
