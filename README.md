<div align="center">
  <img height="200" src="https://i.ibb.co/qMYNww1G/rounded-in-photoretrica-1.png" />
</div>

###

<h1 align="center">pyxcore.language</h1>

###

<div align="center">
  <p>
    <strong>Uma linguagem de programação experimental, limpa e organizada, criada para estudar compiladores, AST, runtime e evolução de linguagens.</strong>
  </p>
</div>

###

<div align="center">

<img src="https://img.shields.io/badge/status-em%20desenvolvimento-111827?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/language-pyxcore-6366f1?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/compiler-python-22c55e?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/runtime-interpreter-f97316?style=for-the-badge&labelColor=000000" />

Official Documentation PyxCore https://pyxcore.base44.app
</div>

---

<h2>
  <img src="https://api.iconify.design/material-symbols/info.svg?color=%236366f1" width="28" />
  Sobre a PyxCore
</h2>

**PyxCore** é uma linguagem de programação experimental em desenvolvimento, criada com foco em clareza, organização e aprendizado sobre construção de compiladores.

O projeto atual possui uma base limpa para transformar código `.pyx` em tokens, gerar uma AST, realizar uma análise semântica inicial e executar o programa por meio de um runtime interpretado.

Esta versão **não inclui IA, Groq, comandos `ask`, LSP, LLVM, JIT, package registry ou website de documentação**. O foco desta fase é estabilizar o núcleo real da linguagem e evitar promessas que ainda não existem no código.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/link.svg?color=%2306b6d4" width="28" />
  Repositório
</h2>

Repositório oficial:

~~~txt
https://github.com/lipeedeveloper/pyxcore
~~~

Clone o projeto:

~~~bash
git clone https://github.com/lipeedeveloper/pyxcore.git
cd pyxcore
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/person.svg?color=%23f97316" width="28" />
  Criador
</h2>

Projeto criado por:

~~~txt
Lipe Developer / Emanuel Felipe
~~~

Usuário do GitHub:

~~~txt
lipeedeveloper
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/checklist.svg?color=%2322c55e" width="28" />
  Estado atual do projeto
</h2>

A PyxCore possui uma base funcional, mas ainda está em desenvolvimento. Abaixo está o estado real desta versão.

### <img src="https://api.iconify.design/material-symbols/check-circle.svg?color=%2322c55e" width="22" /> Implementado

- Lexer funcional;
- Parser funcional;
- AST estruturada;
- Análise semântica inicial;
- Runtime interpretado;
- Bytecode VM simples;
- Formatter simples;
- Test runner para arquivos `.pyx`;
- CLI `pyx`;
- Comando para criar projeto;
- Comando para executar arquivos `.pyx`;
- Comando para verificar código;
- Comando para visualizar tokens;
- Comando para visualizar AST;
- Comando REPL básico;
- Instalador simples para Windows;
- Exemplos em `.pyx`.

### <img src="https://api.iconify.design/material-symbols/science.svg?color=%2306b6d4" width="22" /> Experimental

- VM de bytecode simples;
- REPL inicial;
- Análise semântica básica;
- Formatter por indentação simples.

### <img src="https://api.iconify.design/material-symbols/pending-actions.svg?color=%23facc15" width="22" /> Planejado

- Sistema de tipos;
- Imports e módulos;
- Biblioteca padrão em `.pyx`;
- Melhorias nas mensagens de erro;
- VM com instruction set maior;
- Gerador de bytecode real a partir da AST;
- Debugger integrado;
- Testes automatizados mais completos;
- Documentação técnica expandida.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/target.svg?color=%23ef4444" width="28" />
  Propósito da linguagem
</h2>

A PyxCore foi criada para ser uma linguagem simples de escrever, fácil de entender e boa para estudar como uma linguagem de programação funciona por dentro.

O objetivo principal é construir uma base real e organizada, sem misturar recursos falsos ou incompletos no README.

A PyxCore busca resolver três pontos:

### <img src="https://api.iconify.design/material-symbols/check-circle.svg?color=%2322c55e" width="22" /> Código simples

Sintaxe direta, com funções, variáveis, condições, loops e chamadas de função.

### <img src="https://api.iconify.design/material-symbols/account-tree.svg?color=%2306b6d4" width="22" /> Arquitetura organizada

Separação clara entre lexer, parser, AST, semântica, runtime, VM e ferramentas.

### <img src="https://api.iconify.design/material-symbols/bolt.svg?color=%23facc15" width="22" /> Evolução gradual

A linguagem pode crescer para tipos, módulos, bytecode real, VM maior e futuramente backends mais avançados.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/auto-awesome.svg?color=%23facc15" width="28" />
  Filosofia da PyxCore
</h2>

A filosofia da PyxCore é baseada em uma ideia simples:

> Uma linguagem deve ser pequena o suficiente para entender, organizada o suficiente para crescer e clara o suficiente para evoluir sem virar bagunça.

A linguagem valoriza:

- código limpo;
- sintaxe simples;
- arquitetura modular;
- mensagens de erro melhores ao longo do tempo;
- aprendizado real de compiladores;
- base honesta;
- evolução gradual.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/code-blocks.svg?color=%236366f1" width="28" />
  Exemplo de código
</h2>

Programa simples:

~~~pyx
fn main() {
    println("Bem-vindo ao PyxCore!")
    let nome = "Mundo"
    println("Olá, " + nome + "!")
}
~~~

Função com retorno:

~~~pyx
fn soma(a, b) {
    return a + b
}

fn main() {
    let resultado = soma(10, 20)
    println("Resultado: " + resultado)
}
~~~

Condição:

~~~pyx
fn main() {
    let idade = 18

    if idade >= 18 {
        println("Acesso permitido")
    } else {
        println("Acesso negado")
    }
}
~~~

Repetição:

~~~pyx
fn main() {
    let contador = 0

    while contador < 5 {
        println(contador)
        contador = contador + 1
    }
}
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/account-tree.svg?color=%2306b6d4" width="28" />
  Como a PyxCore funciona
</h2>

A PyxCore segue um pipeline simples:

~~~txt
Código .pyx
    ↓
Lexer
    ↓
Parser
    ↓
AST
    ↓
Análise Semântica
    ↓
Runtime Interpretado
~~~

### <img src="https://api.iconify.design/material-symbols/filter-list.svg?color=%236366f1" width="22" /> Lexer

Transforma o texto do arquivo `.pyx` em tokens.

Exemplo:

~~~pyx
let nome = "PyxCore"
~~~

Gera tokens como:

~~~txt
LET
IDENT
EQUAL
STRING
EOF
~~~

### <img src="https://api.iconify.design/material-symbols/schema.svg?color=%23f97316" width="22" /> Parser

Recebe tokens e monta a AST.

### <img src="https://api.iconify.design/material-symbols/account-tree.svg?color=%2306b6d4" width="22" /> AST

Representa o programa com nós para funções, variáveis, expressões, chamadas, condições, loops e retornos.

### <img src="https://api.iconify.design/material-symbols/rule.svg?color=%2322c55e" width="22" /> Análise semântica

Valida nomes, escopos, funções e variáveis antes da execução.

### <img src="https://api.iconify.design/material-symbols/play-circle.svg?color=%2322c55e" width="22" /> Execução

A execução atual acontece por um interpretador. A VM de bytecode existe como base experimental para evolução futura.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/folder.svg?color=%23facc15" width="28" />
  Estrutura atual do projeto
</h2>

~~~txt
pyxcore/
├── pyxcore/
│   ├── compiler/
│   │   ├── ast.py
│   │   ├── errors.py
│   │   ├── lexer.py
│   │   ├── parser.py
│   │   ├── pipeline.py
│   │   ├── semantic.py
│   │   └── token.py
│   │
│   ├── runtime/
│   │   ├── bytecode.py
│   │   ├── interpreter.py
│   │   └── vm.py
│   │
│   ├── tools/
│   │   ├── formatter.py
│   │   └── test_runner.py
│   │
│   └── cli.py
│
├── examples/
│   ├── hello.pyx
│   ├── math.pyx
│   └── loop.pyx
│
├── tests/
│   └── basic.pyx
│
├── install_pyxcore.cmd
├── install_pyxcore.ps1
├── uninstall_pyxcore.cmd
├── pyproject.toml
├── README.md
└── TEST_RESULT.json
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/download.svg?color=%2322c55e" width="28" />
  Instalação
</h2>

### Instalação pelo Python

~~~bash
pip install -e .
~~~

### Instalação no Windows

Abra o arquivo:

~~~txt
install_pyxcore.cmd
~~~

Depois feche e abra o terminal.

Teste:

~~~bash
pyx doctor
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/terminal.svg?color=%23f97316" width="28" />
  CLI
</h2>

Diagnóstico:

~~~bash
pyx doctor
~~~

Mostrar versão:

~~~bash
pyx --version
~~~

Criar projeto:

~~~bash
pyx new meu_app
cd meu_app
~~~

Executar arquivo `.pyx`:

~~~bash
pyx run main.pyx
~~~

Verificar sintaxe e semântica:

~~~bash
pyx check main.pyx
~~~

Mostrar tokens:

~~~bash
pyx tokens main.pyx
~~~

Mostrar AST:

~~~bash
pyx ast main.pyx
~~~

Formatar arquivo:

~~~bash
pyx fmt main.pyx
~~~

Abrir REPL:

~~~bash
pyx repl
~~~

Rodar testes:

~~~bash
pyx test
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/library-books.svg?color=%236366f1" width="28" />
  Recursos da linguagem
</h2>

A sintaxe atual suporta:

~~~txt
fn
let
return
if / else
while
true / false / null
strings
números
comentários //
operações + - * / %
comparações == != > >= < <=
lógica && || !
funções
chamadas de função
println / print
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/developer-mode.svg?color=%23a855f7" width="28" />
  Ferramentas de desenvolvimento
</h2>

### <img src="https://api.iconify.design/material-symbols/format-align-left.svg?color=%2306b6d4" width="22" /> Formatador

Aplica indentação simples em arquivos `.pyx`.

~~~bash
pyx fmt main.pyx
~~~

### <img src="https://api.iconify.design/material-symbols/science.svg?color=%2322c55e" width="22" /> Test runner

Executa arquivos `.pyx` dentro da pasta de testes.

~~~bash
pyx test
~~~

### <img src="https://api.iconify.design/material-symbols/terminal.svg?color=%23f97316" width="22" /> REPL

Permite testar expressões simples no terminal.

~~~bash
pyx repl
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/science.svg?color=%2322c55e" width="28" />
  Testes
</h2>

Rodar testes pela CLI:

~~~bash
pyx test
~~~

Rodar um exemplo manualmente:

~~~bash
pyx run examples/hello.pyx
pyx run examples/math.pyx
pyx run examples/loop.pyx
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/construction.svg?color=%23f97316" width="28" />
  Roadmap
</h2>

### <img src="https://api.iconify.design/material-symbols/check-circle.svg?color=%2322c55e" width="22" /> Base atual

- [x] Estrutura de package Python;
- [x] CLI `pyx`;
- [x] Lexer;
- [x] Parser;
- [x] AST;
- [x] Análise semântica inicial;
- [x] Runtime interpretado;
- [x] VM de bytecode simples;
- [x] Formatter;
- [x] Test runner;
- [x] Instalador Windows;
- [x] Exemplos `.pyx`.

### <img src="https://api.iconify.design/material-symbols/pending-actions.svg?color=%23facc15" width="22" /> Próximos passos

- [ ] Melhorar mensagens de erro;
- [ ] Criar sistema de tipos;
- [ ] Adicionar imports e módulos;
- [ ] Expandir biblioteca padrão;
- [ ] Gerar bytecode real a partir da AST;
- [ ] Expandir instruction set da VM;
- [ ] Criar debugger integrado;
- [ ] Criar mais testes automatizados;
- [ ] Melhorar documentação técnica.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/warning.svg?color=%23facc15" width="28" />
  O que esta versão não possui
</h2>

Esta versão **não possui**:

- IA integrada;
- comando `pyx ask`;
- Groq API;
- LSP;
- LLVM;
- JIT;
- package registry;
- package manager;
- website de documentação;
- stdlib completa em `.pyx`;
- sistema de tipos completo;
- imports e módulos.

Esses recursos podem ser adicionados futuramente, mas não estão marcados como implementados nesta versão para manter o projeto honesto e profissional.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/groups.svg?color=%2306b6d4" width="28" />
  Contribuição
</h2>

Contribuições são bem-vindas.

Você pode ajudar com:

- correção de bugs;
- exemplos `.pyx`;
- testes;
- documentação;
- melhorias no parser;
- melhorias no runtime;
- melhorias na VM;
- melhorias na CLI.

Fluxo básico:

~~~bash
git checkout -b minha-feature
git add .
git commit -m "feat: adiciona nova funcionalidade"
git push origin minha-feature
~~~

Depois, abra um Pull Request no repositório:

~~~txt
https://github.com/lipeedeveloper/pyxcore
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/bug-report.svg?color=%23ef4444" width="28" />
  Reportar problemas
</h2>

Caso encontre algum erro, abra uma issue:

~~~txt
https://github.com/lipeedeveloper/pyxcore/issues
~~~

Inclua:

- descrição do problema;
- código que causou o erro;
- mensagem de erro recebida;
- comportamento esperado;
- sistema operacional;
- versão do Python;
- passos para reproduzir.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/security.svg?color=%2322c55e" width="28" />
  Licença
</h2>

Este projeto pode ser distribuído sob a licença MIT.

~~~txt
MIT License

Copyright (c) 2026 PyxCore

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the software.
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/favorite.svg?color=%23ef4444" width="28" />
  Apoie o projeto
</h2>

Se você gostou da PyxCore, considere deixar uma estrela no repositório:

~~~txt
https://github.com/lipeedeveloper/pyxcore
~~~

---

<div align="center">

<h2>
  <img src="https://api.iconify.design/material-symbols/code.svg?color=%236366f1" width="28" />
  pyxcore.language
</h2>

<p>
  <strong>Uma linguagem simples na entrada, organizada na base e honesta na evolução.</strong>
</p>

<br/>

<img src="https://img.shields.io/badge/made%20with-code-6366f1?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/built%20with-caf%C3%A9%20e%20persist%C3%AAncia-f97316?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/project-pyxcore-22c55e?style=for-the-badge&labelColor=000000" />

</div>
