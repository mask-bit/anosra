# Guia de Instalação Rápida - Anosra Backend

## Passo 1: Instalar Dependências

```bash
pip install -r requirements.txt
```

## Passo 2: Configurar Variáveis de Ambiente (Opcional)

O sistema já vem configurado para usar SQLite por padrão. Se quiser customizar:

```bash
cp .env.example .env
# Edite o arquivo .env se necessário
```

## Passo 3: Rodar o Servidor

```bash
python run.py
```

O servidor iniciará em `http://localhost:5000`

Na primeira execução, o banco de dados SQLite será criado automaticamente em `anosra.db`

## Testar se está funcionando

Abra o navegador em: `http://localhost:5000/api/health`

Você deve ver: `{"status": "ok"}`

## Próximos Passos

1. Abra os arquivos HTML em `frontend/templates/` no navegador
2. Faça cadastro de um novo usuário
3. Comece a usar o sistema!

## Problemas Comuns

### Erro de porta em uso
Se a porta 5000 já estiver em uso, edite `run.py` e mude para outra porta (ex: 5001)

### Módulos não encontrados
Certifique-se de ter instalado todas as dependências: `pip install -r requirements.txt`
