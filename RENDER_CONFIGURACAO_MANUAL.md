# 🚀 Guia de Configuração Manual do Render para Anosra

## ✅ Problema Resolvido
O arquivo `requirements.txt` agora está na raiz do projeto e o sistema está pronto para deploy.

---

## 📋 Passo a Passo - Configuração Manual no Render

### 1. Criar Novo Web Service
- Acesse: https://dashboard.render.com
- Clique em **"New +"** → **"Web Service"**
- Conecte seu repositório GitHub: `mask-bit/anosra`

### 2. Configurações Básicas

**Nome do Serviço:**
```
anosra
```

**Região:**
```
Oregon (US West)
```

**Branch:**
```
main
```

**Root Directory:**
```
(deixe em branco)
```

### 3. Ambiente e Comandos

**Environment:**
```
Python 3
```

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
cd backend && gunicorn wsgi:app --bind 0.0.0.0:$PORT
```

### 4. Variáveis de Ambiente (Environment Variables)

Adicione as seguintes variáveis clicando em **"Add Environment Variable"**:

| Key | Value |
|-----|-------|
| `FLASK_ENV` | `production` |
| `SECRET_KEY` | `sua-chave-secreta-segura-aqui-123456` |
| `DATABASE_URL` | `sqlite:///anosra.db` |

**IMPORTANTE:** Gere uma SECRET_KEY forte. Você pode usar:
```python
import secrets
secrets.token_hex(32)
```

### 5. Plano

**Instance Type:**
```
Free
```

### 6. Deploy

Clique em **"Create Web Service"** e aguarde o deploy (leva 2-5 minutos).

---

## ✅ Checklist de Verificação

Após o deploy, verifique:

- [ ] Build completou sem erros
- [ ] Service está "Live" (verde)
- [ ] Acesse a URL: `https://anosra.onrender.com`
- [ ] Página inicial carrega corretamente
- [ ] Links de navegação funcionam
- [ ] Login/cadastro aparecem

---

## 🔧 Estrutura de Arquivos para Deploy

```
anosra/
├── requirements.txt          ← Na raiz (já está correto)
├── Procfile                  ← Backup para Heroku
├── runtime.txt               ← Versão Python
├── backend/
│   ├── wsgi.py              ← Entry point
│   ├── run.py               ← Dev server
│   ├── app/
│   │   ├── __init__.py      ← Flask app
│   │   ├── config.py        ← Configurações
│   │   ├── models/          ← Database models
│   │   ├── routes/          ← API endpoints
│   │   └── services/        ← Business logic
│   └── requirements.txt     ← Backup (não usado)
└── frontend/
    ├── templates/           ← HTML pages
    └── static/             ← CSS, JS, images
```

---

## 🐛 Solução de Problemas

### Erro: "Could not open requirements file"
✅ **RESOLVIDO** - O arquivo requirements.txt agora está na raiz

### Erro: "Module not found"
**Solução:** Verifique se todas as dependências estão no requirements.txt

### Erro: "Application failed to start"
**Verificar:**
1. Start Command está correto: `cd backend && gunicorn wsgi:app --bind 0.0.0.0:$PORT`
2. Arquivo `backend/wsgi.py` existe
3. Variáveis de ambiente configuradas

### Site carrega mas páginas não funcionam
**Verificar:**
1. Templates estão em `frontend/templates/`
2. Static files em `frontend/static/`
3. Rotas configuradas em `backend/app/__init__.py`

---

## 📊 Monitoramento

Após deploy bem-sucedido:

1. **Logs ao vivo:** Dashboard → Logs
2. **Métricas:** Dashboard → Metrics
3. **Shell:** Dashboard → Shell (para debug)

---

## 🔄 Atualizações Futuras

Quando fizer mudanças no código:

1. Faça push para GitHub
2. Render detecta automaticamente
3. Deploy automático em ~2 minutos

---

## 💡 Dicas

- **Free tier:** 750 horas/mês grátis
- **Sleep após inatividade:** 15 minutos sem requests
- **Primeira request após sleep:** ~30 segundos
- **SSL automático:** HTTPS configurado automaticamente

---

## 🎯 URLs do Sistema

Após deploy, suas páginas estarão em:

- Landing: `https://anosra.onrender.com/`
- Login: `https://anosra.onrender.com/login`
- Cadastro: `https://anosra.onrender.com/cadastro`
- Dashboard: `https://anosra.onrender.com/dashboard`
- Negócios: `https://anosra.onrender.com/negocios`
- Despesas: `https://anosra.onrender.com/despesas`
- Funcionários: `https://anosra.onrender.com/funcionarios`
- Relatórios: `https://anosra.onrender.com/relatorios`
- Integração: `https://anosra.onrender.com/integracao`
- Configurações: `https://anosra.onrender.com/configuracoes`

---

## ✅ Sistema Pronto

O Anosra está configurado corretamente para deploy no Render. Após seguir este guia, seu sistema estará online e funcionando perfeitamente!
