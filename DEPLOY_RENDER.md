# Deploy no Render - Anosra

## Passo a Passo

### 1. Preparar o Repositório
Certifique-se que o código está no GitHub com todos os arquivos:
- `backend/requirements.txt` (com gunicorn)
- `render.yaml` (configuração do Render)
- `Procfile` (comando de inicialização)
- `backend/wsgi.py` (entry point)

### 2. Criar Conta no Render
1. Acesse [render.com](https://render.com)
2. Crie uma conta gratuita
3. Conecte sua conta GitHub

### 3. Novo Web Service
1. Clique em "New +" → "Web Service"
2. Conecte seu repositório GitHub (mask-bit/Anosra)
3. Configure:
   - **Name**: anosra
   - **Environment**: Python 3
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && gunicorn wsgi:app --bind 0.0.0.0:$PORT`

### 4. Variáveis de Ambiente
Adicione no painel do Render:
```
FLASK_ENV=production
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///anosra.db
```

### 5. Deploy
- Clique em "Create Web Service"
- Aguarde o build (3-5 minutos)
- Acesse a URL fornecida pelo Render

## URLs Disponíveis
Após deploy, você terá:
- `https://anosra.onrender.com/` - Landing page
- `https://anosra.onrender.com/login` - Login
- `https://anosra.onrender.com/dashboard` - Dashboard
- `https://anosra.onrender.com/api/auth/register` - API de cadastro
- `https://anosra.onrender.com/api/auth/login` - API de login

## Problemas Comuns

### Build Failed
- Verifique se `requirements.txt` está em `backend/`
- Confirme que todas as dependências estão listadas

### App Crashed
- Verifique se o comando start está correto
- Confirme que `wsgi.py` existe em `backend/`
- Veja os logs no painel do Render

### Database Error
- SQLite funciona no Render Free Tier
- Para PostgreSQL, crie um banco separado no Render

## Atualizar Deployment
Qualquer push para `main` no GitHub atualiza automaticamente.

## Custos
- **Free Tier**: Serviço dorme após 15min de inatividade
- **Starter ($7/mês)**: Sempre ativo, mais recursos

## Suporte
Documentação oficial: [render.com/docs](https://render.com/docs)
