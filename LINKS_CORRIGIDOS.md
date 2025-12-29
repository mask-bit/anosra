# Links de Navegação Corrigidos

Todos os links de navegação nos arquivos HTML foram atualizados para usar as rotas Flask corretas.

## Mudanças Realizadas

### Links HTML
Todos os links `href` foram atualizados:
- `href="login.html"` → `href="/login"`
- `href="cadastro.html"` → `href="/cadastro"`
- `href="dashboard.html"` → `href="/dashboard"`
- `href="negocios.html"` → `href="/negocios"`
- `href="despesas.html"` → `href="/despesas"`
- `href="funcionarios.html"` → `href="/funcionarios"`
- `href="relatorios.html"` → `href="/relatorios"`
- `href="integracao.html"` → `href="/integracao"`
- `href="configuracoes.html"` → `href="/configuracoes"`
- `href="recuperar-senha.html"` → `href="/recuperar-senha"`

### Links JavaScript
Todos os redirecionamentos JavaScript foram atualizados:
- `window.location.href = 'dashboard.html'` → `window.location.href = '/dashboard'`
- `window.location.href = 'negocios.html'` → `window.location.href = '/negocios'`
- `window.location.href = 'login.html'` → `window.location.href = '/login'`
- E assim por diante para todas as páginas

## Como Executar o Script

Se precisar executar novamente o script de correção:

```bash
cd anosra
python scripts/fix_links.py
```

## Rotas Flask Disponíveis

Todas as seguintes rotas estão configuradas e funcionando:

- `/` - Landing page (index.html)
- `/login` - Página de login
- `/cadastro` - Página de cadastro
- `/dashboard` - Dashboard principal
- `/negocios` - Gestão de negócios
- `/despesas` - Controle de despesas
- `/funcionarios` - Gestão de funcionários
- `/relatorios` - Relatórios e análises
- `/integracao` - Integração Open Finance
- `/configuracoes` - Configurações do sistema
- `/recuperar-senha` - Recuperação de senha

## Testando a Navegação

1. Inicie o servidor Flask:
   ```bash
   cd backend
   python run.py
   ```

2. Acesse http://localhost:5000

3. Todos os botões e links de navegação agora devem funcionar corretamente!

## Problemas Conhecidos

Se algum link ainda não funcionar, verifique:
1. O servidor Flask está rodando?
2. Você está acessando através de `http://localhost:5000` (não abrindo os arquivos HTML diretamente)?
3. O console do navegador mostra algum erro?
</parameter>
