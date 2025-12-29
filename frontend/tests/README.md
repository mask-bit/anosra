# Testes do Frontend

Diretório reservado para testes do frontend da aplicação Anosra.

## Estrutura Planejada

```
tests/
├── unit/           # Testes unitários de funções
├── integration/    # Testes de integração com API
└── e2e/           # Testes end-to-end
```

## Ferramentas Sugeridas

- Jest para testes unitários
- Testing Library para testes de componentes
- Cypress ou Playwright para testes E2E

## Como Executar

```bash
# Instalar dependências de teste
npm install --save-dev jest @testing-library/dom

# Executar testes
npm test
