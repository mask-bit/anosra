# Deploy do Anosra no Render - Passo a Passo

## Problema Resolvido
O Render estava tentando fazer deploy como Node.js por causa de arquivos package.json desnecessários. Esses arquivos foram removidos.

## Configuração Manual no Render (Recomendado)

### 1. Criar Novo Web Service
- Acesse: https://dashboard.render.com/
- Clique em "New +" > "Web Service"
- Conecte seu repositório GitHub: `mask-bit/anosra`

### 2. Configurações do Serviço

**Informações Básicas:**
- Name: `anosra`
- Region: `Oregon (US West)` (ou qualquer outra)
- Branch: `main`

**Build & Deploy:**
- Environment: `Python 3`
- Build Command: `pip install -r backend/requirements.txt`
- Start Command: `cd backend && gunicorn wsgi:app --bind 0.0.0.0:$PORT`

**Diretório de Publicações:**
- Deixe VAZIO (não preencha nada)

### 3. Variáveis de Ambiente

Adicione estas variáveis (clique em "Add Environment Variable"):

```
FLASK_ENV=production
SECRET_KEY=sua-chave-secreta-aqui-gere-uma-aleatoria
DATABASE_URL=sqlite:///anosra.db
PYTHON_VERSION=3.11.0
```

Para gerar uma SECRET_KEY segura, use:
```python
import secrets
print(secrets.token_hex(32))
```

### 4. Plano
- Selecione: `Free`

### 5. Deploy
- Clique em "Create Web Service"
- Aguarde o deploy (pode levar 3-5 minutos)

## Após o Deploy

Seu sistema estará disponível em:
```
https://anosra.onrender.com
```

### Páginas Disponíveis:
- `/` - Landing page
- `/login` - Login
- `/cadastro` - Cadastro
- `/dashboard` - Dashboard
- `/negocios` - Negócios
- `/despesas` - Despesas
- `/funcionarios` - Funcionários
- `/relatorios` - Relatórios
- `/integracao` - Integração Open Finance
- `/configuracoes` - Configurações

## Solução de Problemas

### Se o build falhar:
1. Verifique se o Build Command está correto
2. Confirme que o Start Command tem `cd backend &&`
3. Certifique-se de que Environment está como "Python 3"

### Se aparecer erro 404:
1. Verifique se o Start Command está correto
2. Confirme que a porta está configurada com `$PORT`

### Para ver logs:
- No dashboard do Render, clique em "Logs"
- Logs em tempo real mostrarão erros

## Banco de Dados

O sistema usa SQLite por padrão (arquivo local). Para produção, considere:
- PostgreSQL (Render oferece banco gratuito)
- Supabase
- Neon

Para trocar para PostgreSQL:
1. Crie um banco PostgreSQL no Render
2. Atualize a variável `DATABASE_URL` com a connection string
3. Adicione `psycopg2-binary` ao requirements.txt

## Importante

O deploy pode demorar 3-5 minutos na primeira vez. Seja paciente!
