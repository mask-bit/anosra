# ANOSRA - Deploy Instructions

## O Problema Atual

O Vercel está tentando fazer build como projeto **Node.js/Next.js**, mas o Anosra é **Python/Flask**.

## Solução Imediata

### Opção A: Use o Render (RECOMENDADO)

O Render é a plataforma ideal para Flask. Configuração simples:

1. Vá para https://render.com
2. Crie um novo "Web Service"
3. Conecte seu repositório GitHub
4. Configure:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && gunicorn wsgi:app --bind 0.0.0.0:$PORT`
5. Adicione variáveis de ambiente:
   - `FLASK_ENV=production`
   - `SECRET_KEY=sua-chave-secreta-123`
   - `DATABASE_URL=sqlite:///anosra.db`

### Opção B: Configure o Vercel Manualmente

Se preferir continuar no Vercel:

1. **No GitHub**: Faça commit das alterações (package.json foi removido)
2. **No Vercel Dashboard**:
   - Vá em Settings > General
   - **Framework Preset**: Other
   - **Build Command**: Deixe vazio
   - **Output Directory**: Deixe vazio
   - **Install Command**: `pip install -r backend/requirements.txt`

3. **Em Environment Variables** adicione:
   ```
   FLASK_ENV=production
   SECRET_KEY=sua-chave-super-secreta
   DATABASE_URL=sqlite:///anosra.db
   PYTHONPATH=backend
   ```

4. **Importante**: No arquivo `vercel.json` já está configurado para Python

## Por Que o Erro Aconteceu?

O v0 gerou o projeto inicialmente com arquivos Next.js (`package.json`, `tsconfig.json`). Esses arquivos faziam o Vercel pensar que era um projeto Node.js. Agora foram removidos.

## Estrutura Correta

```
anosra/
├── backend/              # Backend Python/Flask
│   ├── app/
│   ├── wsgi.py          # Entry point
│   ├── run.py
│   └── requirements.txt
├── frontend/            # Frontend HTML/CSS/JS
│   ├── templates/
│   └── static/
└── vercel.json         # Configuração Python
```

## Teste Local

Antes de fazer deploy, teste localmente:

```bash
cd backend
pip install -r requirements.txt
python run.py
```

Acesse: http://localhost:5000

## Deploy Recommendations

| Plataforma | Ideal Para | Dificuldade |
|-----------|------------|-------------|
| **Render** | Flask/Python | Fácil |
| Vercel | Next.js/Node | Médio para Flask |
| Railway | Qualquer stack | Fácil |
| Heroku | Qualquer stack | Médio |

**Recomendação**: Use o Render para melhor experiência com Flask.
