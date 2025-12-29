# Guia Definitivo de Deploy - Anosra

## ⚠️ Por que o Vercel NÃO funciona?

O erro `FUNCTION_INVOCATION_FAILED` acontece porque:

- **Anosra é Flask tradicional**: Precisa de servidor web rodando continuamente
- **Vercel é para Serverless**: Otimizado para Next.js e funções que executam sob demanda
- **Incompatibilidade fatal**: Flask precisa manter estado, conexões de banco e sessões ativas

**Solução**: Use Render, Railway ou Heroku - plataformas feitas para aplicações Python/Flask.

---

## ✅ OPÇÃO 1: RENDER (Recomendado)

### Por que Render?
- Suporte nativo para Python/Flask
- Deploy gratuito ilimitado
- SSL automático grátis
- PostgreSQL gratuito incluído
- Deploy em 5 minutos

### Passo a Passo:

**1. Acesse Render**
- Vá para: https://render.com
- Faça login com sua conta GitHub

**2. Criar Web Service**
- Clique em **"New +"** → **"Web Service"**
- Conecte seu repositório: `mask-bit/anosra`
- Clique em **"Connect"**

**3. Configurações do Deploy**
```
Name: anosra
Region: Oregon (US West)
Branch: main
Root Directory: (deixe vazio)
Runtime: Python 3
Build Command: pip install -r backend/requirements.txt
Start Command: cd backend && gunicorn wsgi:app --bind 0.0.0.0:$PORT
Instance Type: Free
```

**4. Variáveis de Ambiente** (clique em "Advanced" antes de criar)
```
FLASK_ENV=production
SECRET_KEY=sua-chave-secreta-super-complexa-123456789
DATABASE_URL=sqlite:///anosra.db
PYTHON_VERSION=3.11.0
```

**5. Criar Web Service**
- Clique em **"Create Web Service"**
- Aguarde 3-5 minutos

**6. Acessar**
- Seu app estará disponível em: `https://anosra.onrender.com`

---

## ✅ OPÇÃO 2: RAILWAY

### Passo a Passo:

**1. Criar Conta**
- Acesse: https://railway.app
- Faça login com GitHub

**2. Novo Projeto**
- Clique em **"New Project"**
- Selecione **"Deploy from GitHub repo"**
- Escolha: `mask-bit/anosra`

**3. Configurar Variáveis**
Railway detecta Python automaticamente. Adicione:
```
FLASK_ENV=production
SECRET_KEY=sua-chave-secreta-aqui
PORT=5000
```

**4. Gerar Domínio**
- Vá em **Settings → Networking**
- Clique em **"Generate Domain"**

**5. Deploy Automático**
Railway faz o resto automaticamente!

---

## ✅ OPÇÃO 3: HEROKU

### Comandos no Terminal:

```bash
# 1. Instalar Heroku CLI
# Download: https://devcenter.heroku.com/articles/heroku-cli

# 2. Login
heroku login

# 3. Criar aplicação
heroku create anosra-app

# 4. Configurar variáveis
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=sua-chave-secreta-complexa

# 5. Deploy
git push heroku main

# 6. Abrir aplicação
heroku open
```

---

## ❌ O que NÃO funciona

### Vercel
- Erro: `FUNCTION_INVOCATION_FAILED`
- Motivo: Flask não é serverless
- Status: Incompatível

### Netlify
- Motivo: Apenas sites estáticos
- Status: Não suporta Python backend

---

## 🧪 Testar Localmente Antes

```bash
# 1. Navegar para backend
cd backend

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar ambiente
cp .env.example .env
# Edite o .env com suas configurações

# 4. Iniciar servidor
python run.py

# 5. Acessar aplicação
# http://localhost:5000
```

---

## 📋 Checklist Pré-Deploy

- [ ] Repositório GitHub atualizado
- [ ] `backend/requirements.txt` contém todas as dependências
- [ ] `backend/wsgi.py` existe e está correto
- [ ] Variáveis de ambiente definidas
- [ ] Testado localmente com sucesso

---

## 🌐 URLs Disponíveis no App

### Páginas Frontend
- `/` - Landing page
- `/login` - Login
- `/cadastro` - Cadastro de usuário
- `/dashboard` - Dashboard principal
- `/negocios` - Gestão de negócios
- `/despesas` - Controle de despesas
- `/funcionarios` - Gestão de funcionários
- `/relatorios` - Relatórios e análises
- `/integracao` - Integrações Open Finance
- `/configuracoes` - Configurações do sistema
- `/recuperar-senha` - Recuperação de senha

### API Endpoints
- `POST /api/auth/register` - Registro de usuário
- `POST /api/auth/login` - Login
- `POST /api/negocios` - Criar negócio
- `GET /api/negocios` - Listar negócios
- `GET /api/despesas` - Listar despesas
- `POST /api/despesas` - Criar despesa

---

## 🔧 Troubleshooting

### Erro: "Module not found"
```bash
# Reinstalar dependências
pip install -r backend/requirements.txt
```

### Erro: "Database error"
```bash
# SQLite cria automaticamente
# Se persistir, delete anosra.db e reinicie
rm backend/anosra.db
python backend/run.py
```

### Erro: "Port already in use"
```python
# Mude a porta no run.py
app.run(debug=True, port=5001)
```

### Logs no Render
- Dashboard → Logs → Ver em tempo real

---

## 🚀 Próximos Passos Pós-Deploy

1. **Domínio Customizado**
   - Configure seu domínio próprio no Render

2. **Banco de Dados PostgreSQL**
   - Para produção séria, migre do SQLite

3. **Email Configuration**
   - Configure SMTP para recuperação de senha

4. **Monitoramento**
   - Configure alertas de uptime

5. **Backup Automático**
   - Configure backup do banco de dados

---

## 📞 Suporte

**Problemas no Deploy?**
1. Verifique os logs na plataforma escolhida
2. Confirme todas as variáveis de ambiente
3. Teste localmente primeiro
4. Verifique se requirements.txt está completo

---

**Recomendação Final**: Use o **Render** - é gratuito, simples e perfeito para Flask!
