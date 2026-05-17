# Contributing to PyxCore

Obrigado por ajudar a melhorar o PyxCore! Este documento descreve como colaborar com o projeto e enviar contribuições.

## Repositório

https://github.com/lipeedeveloper/pyxcore

## Como contribuir

1. Faça um fork do repositório.
2. Crie uma branch com um nome descritivo:
   - `feature/nova-sintaxe`
   - `bugfix/lexer-fix`
3. Faça suas alterações e teste localmente:
   - `python tests/test_compiler.py`
4. Mantenha o código claro e documentado.
5. Abra um pull request para a branch `main` do repositório original.

## Estilo de código

- Use `snake_case` para variáveis e funções
- Use `CamelCase` para nomes de classes
- Comente trechos complexos e mantenha a estrutura simples
- Prefira código legível em vez de otimizações prematuras

## Testes

Execute os testes antes de enviar sua contribuição:

```bash
python tests/test_compiler.py
```

Se você adicionar novas funcionalidades, inclua testes correspondentes no `tests/`.

## Issue e Pull Requests

- Abra issues para bugs, ideias e melhorias
- Um PR deve ter descrição clara e tests quando necessário
- Cite o problema ou issue que o PR resolve

## Desenvolvimento

- Para rodar o compilador manualmente:
  - `python compiler/pyxc.py examples/hello.pyx`
- Para gerar o pacote de release:
  - `make package`

## Código aberto

PyxCore é licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para detalhes.
