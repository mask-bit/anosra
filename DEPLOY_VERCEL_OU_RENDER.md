# Deploy do Anosra - Guia Completo

## IMPORTANTE: Vercel vs Render

O Anosra é uma aplicação **Python/Flask**, não Node.js/Next.js.

### Opção 1: Render (RECOMENDADO para Flask)

**Por que Render?**
- Suporte nativo a Python/Flask
- Banco de dados SQLite funciona direto
- Configuração mais simples
- Melhor para aplicações backend

**Passos no Render:**

1. Acesse https://render.com e faça login
2. Clique em "New +" e selecione "Web Service"
3. Conecte seu repositório GitHub
4. Configure:
   - **Name**: anosra
   - **Environment**: Python 3
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && gunicorn wsgi:app --bind 0.0.0.0:$PORT`
   - **Instance Type**: Free

5. Adicione as variáveis de ambiente:
   ```
   FLASK_ENV=production
   SECRET_KEY=sua-chave-super-secreta-aqui-12345
   DATABASE_URL=sqlite:///anosra.db
   ```

6. Clique em "Create Web Service"

### Opção 2: Vercel (Funciona mas não é ideal)

O Vercel é otimizado para Next.js, mas pode rodar Python com limitações.

**Configuração já incluída:**
- `vercel.json` configurado para Python
- Rotas para servir arquivos estáticos
- Build configurado para Flask

**No painel do Vercel:**
1. Vá em Settings > General
2. Em "Build & Development Settings":
   - Framework Preset: Other
   - Build Command: `pip install -r backend/requirements.txt`
   - Output Directory: (deixe vazio)

3. Em Environment Variables adicione:
   ```
   FLASK_ENV=production
   SECRET_KEY=sua-chave-secreta
   DATABASE_URL=sqlite:///anosra.db
   ```

### Opção 3: Railway

```bash
# Instale a CLI do Railway
npm i -g @railway/cli

# Faça login
railway login

# Inicie o projeto
railway init

# Configure
railway up
```

### Opção 4: Heroku

```bash
# No seu terminal
heroku login
heroku create anosra-app
git push heroku main
```

## Recomendação Final

**Use o Render** - É a melhor plataforma para Flask:
- Free tier generoso
- Deploy automático do GitHub
- Logs em tempo real
- Fácil configuração

## Problemas Comuns

### Erro: "Module not found"
- Verifique se o `requirements.txt` está completo
- Certifique-se que o build command está correto

### Erro: "Application failed to start"
- Verifique as variáveis de ambiente
- Confirme que o comando start está apontando para `backend/wsgi.py`

### Erro: "Database not found"
- No Render/Railway: O SQLite funcionará automaticamente
- No Vercel: SQLite tem limitações, considere usar PostgreSQL

## Estrutura do Projeto

```
anosra/
├── backend/
│   ├── app/
│   ├── wsgi.py          # Entry point para produção
│   ├── run.py           # Entry point para desenvolvimento
│   └── requirements.txt # Dependências Python
├── frontend/
│   ├── templates/       # Arquivos HTML
│   └── static/          # CSS, JS, imagens
└── vercel.json         # Configuração Vercel (opcional)
