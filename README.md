<div align="center">
  <img height="200" src="https://i.ibb.co/qMYNww1G/rounded-in-photoretrica-1.png" />
</div>

###

<h1 align="center">pyxcore.language</h1>

###

<div align="center">
  <p>
    <strong>Uma linguagem de programação moderna, expressiva e em desenvolvimento, criada para transformar ideias, café e persistência em sistemas reais.</strong>
  </p>
</div>

###

<div align="center">

<img src="https://img.shields.io/badge/status-em%20desenvolvimento-111827?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/language-pyxcore-6366f1?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/compiler-pyx%20compiler-22c55e?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/runtime-python%20vm-f97316?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/focus-tooling-06b6d4?style=for-the-badge&labelColor=000000" />
<h1 align="center">Inspirações:</h1>

###

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" height="40" alt="mongodb logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" height="40" alt="mysql logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" height="40" alt="cplusplus logo"  />
</div>

###
</div>

###

<div align="center">
  <p>
    <img src="https://api.iconify.design/material-symbols/code.svg?color=%236366f1" width="20" />
    Simples para começar.
    <img src="https://api.iconify.design/material-symbols/account-tree.svg?color=%2306b6d4" width="20" />
    Organizada para crescer.
    <img src="https://api.iconify.design/material-symbols/rocket-launch.svg?color=%2322c55e" width="20" />
    Preparada para evoluir.
  </p>
</div>

---

<h2>
  <img src="https://api.iconify.design/material-symbols/info.svg?color=%236366f1" width="28" />
  Sobre a PyxCore
</h2>

**PyxCore** é uma linguagem de programação em desenvolvimento, criada com foco em clareza, organização, aprendizado de compiladores e evolução técnica.

O projeto foi pensado para servir como uma base real de linguagem, com compilador próprio, runtime experimental, biblioteca padrão inicial, ferramentas de desenvolvimento e uma estrutura preparada para crescer com o tempo.

A PyxCore ainda não é uma linguagem pronta para produção. Ela está em fase de construção e evolução, com recursos funcionais, módulos experimentais e partes planejadas para versões futuras.

O objetivo do projeto é construir uma linguagem com identidade própria, mantendo uma base simples de entender, fácil de modificar e organizada o suficiente para receber recursos avançados no futuro.

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

A PyxCore possui uma base funcional, mas ainda está em desenvolvimento. As partes abaixo representam o estado real do projeto.

### <img src="https://api.iconify.design/material-symbols/check-circle.svg?color=%2322c55e" width="22" /> Implementado

- Lexer funcional para tokens básicos da linguagem;
- Parser funcional para funções, variáveis, chamadas, blocos, condicionais, loops e retornos;
- AST com nós estruturados;
- Analisador semântico inicial com escopos e símbolos;
- Interpretador simples para executar AST;
- VM de bytecode baseada em stack;
- Biblioteca padrão inicial em Python;
- CLI instalável via `pyproject.toml`;
- Comandos para executar código, visualizar tokens, visualizar AST, formatar arquivos e rodar testes;
- Formatador simples para arquivos `.pyx`;
- Test runner usando `unittest`;
- LSP experimental com autocomplete, hover e diagnósticos básicos;
- Package registry local experimental usando FastAPI;
- Backend LLVM experimental usando `llvmlite`;
- JIT experimental usando `llvmlite`;
- Garbage collector experimental baseado em mark-and-sweep simulado;
- Documentação local em Markdown;
- Exemplos em `.pyx`.

### <img src="https://api.iconify.design/material-symbols/science.svg?color=%2306b6d4" width="22" /> Experimental

- LLVM backend;
- LLVM JIT;
- Garbage collector;
- Package registry;
- LSP;
- Pattern matching;
- Generics;
- Otimizações SSA;
- Debugger.

Essas partes existem como base técnica, mas ainda não representam uma implementação completa de linguagem de produção.

### <img src="https://api.iconify.design/material-symbols/pending-actions.svg?color=%23facc15" width="22" /> Planejado

- Sistema de tipos completo;
- Imports e módulos integrados ao parser principal;
- Biblioteca padrão em `.pyx`;
- Integração completa da AST com LLVM;
- VM com instruction set maior;
- Debugger integrado à VM;
- LSP completo seguindo o protocolo oficial;
- Package manager com lockfile;
- Registry de pacotes mais robusto;
- Mais testes automatizados;
- Documentação técnica expandida.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/target.svg?color=%23ef4444" width="28" />
  Propósito da linguagem
</h2>

A PyxCore foi criada para ser uma linguagem simples de escrever, fácil de entender e preparada para crescer de forma organizada.

O propósito principal é reduzir complexidade desnecessária sem limitar a evolução técnica do projeto. A ideia é permitir que o código seja limpo, previsível e agradável de manter.

A PyxCore busca resolver três pontos importantes:

### <img src="https://api.iconify.design/material-symbols/check-circle.svg?color=%2322c55e" width="22" /> Código mais claro

A linguagem valoriza uma sintaxe objetiva, onde cada parte do código tenha uma intenção fácil de entender.

### <img src="https://api.iconify.design/material-symbols/account-tree.svg?color=%2306b6d4" width="22" /> Organização desde a base

O projeto foi estruturado com módulos separados para compilador, runtime, stdlib, VM, LSP, testes e ferramentas.

### <img src="https://api.iconify.design/material-symbols/bolt.svg?color=%23facc15" width="22" /> Evolução técnica

A arquitetura permite evoluir para recursos como bytecode, LLVM IR, JIT, generics, pattern matching e gerenciamento de memória.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/auto-awesome.svg?color=%23facc15" width="28" />
  Filosofia da PyxCore
</h2>

A filosofia da PyxCore é baseada em uma ideia simples:

> Uma linguagem deve ser fácil o suficiente para começar, organizada o suficiente para crescer e poderosa o suficiente para evoluir.

A linguagem valoriza:

- código limpo e legível;
- sintaxe simples e expressiva;
- estrutura interna organizada;
- mensagens de erro compreensíveis;
- crescimento gradual;
- ferramentas integradas;
- boa experiência para o desenvolvedor;
- base preparada para estudos e projetos reais;
- liberdade para evoluir sem perder simplicidade.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/code-blocks.svg?color=%236366f1" width="28" />
  Exemplo de código
</h2>

Programa simples:

~~~pyx
fn main() {
    print("Olá, PyxCore!")
}
~~~

Função com retorno:

~~~pyx
fn soma(a, b) {
    return a + b
}

fn main() {
    let resultado = soma(10, 20)
    print(resultado)
}
~~~

Condição:

~~~pyx
fn main() {
    let idade = 18

    if idade >= 18 {
        print("Acesso permitido")
    } else {
        print("Acesso negado")
    }
}
~~~

Repetição:

~~~pyx
fn main() {
    let contador = 0

    while contador < 5 {
        print(contador)
        contador = contador + 1
    }
}
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/account-tree.svg?color=%2306b6d4" width="28" />
  Como a PyxCore funciona
</h2>

A PyxCore segue uma estrutura de compilação organizada.

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
Interpretador / VM experimental
    ↓
Runtime / Stdlib
~~~

### <img src="https://api.iconify.design/material-symbols/filter-list.svg?color=%236366f1" width="22" /> Lexer

O lexer lê o código-fonte e transforma caracteres em tokens.

Exemplo:

~~~pyx
let nome = "PyxCore"
~~~

Pode ser transformado em:

~~~txt
LET
IDENTIFIER
EQUAL
STRING
~~~

### <img src="https://api.iconify.design/material-symbols/schema.svg?color=%23f97316" width="22" /> Parser

O parser recebe tokens e constrói uma AST.

### <img src="https://api.iconify.design/material-symbols/account-tree.svg?color=%2306b6d4" width="22" /> AST

A AST representa o programa de forma estruturada, com nós para funções, variáveis, expressões, chamadas, condições, loops e retornos.

### <img src="https://api.iconify.design/material-symbols/rule.svg?color=%2322c55e" width="22" /> Análise semântica

A análise semântica verifica se o código faz sentido além da sintaxe.

Ela pode validar:

- variáveis declaradas;
- funções existentes;
- escopos;
- chamadas de função;
- atribuições;
- erros antes da execução.

### <img src="https://api.iconify.design/material-symbols/play-circle.svg?color=%2322c55e" width="22" /> Execução

A execução atual pode acontecer por um interpretador simples. Também existe uma VM de bytecode experimental para evolução futura.

### <img src="https://api.iconify.design/material-symbols/memory.svg?color=%23a855f7" width="22" /> LLVM experimental

O projeto possui um backend LLVM experimental com `llvmlite`. Atualmente ele serve como base para estudos e testes de JIT, ainda sem integração completa com todos os nós da AST.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/folder.svg?color=%23facc15" width="28" />
  Estrutura atual do projeto
</h2>

~~~txt
pyxcore/
├── pyxcore/
│   ├── compiler/
│   │   ├── lexer.py
│   │   ├── parser.py
│   │   ├── ast_nodes.py
│   │   ├── semantic.py
│   │   ├── interpreter.py
│   │   ├── pipeline.py
│   │   ├── formatter.py
│   │   ├── llvm_backend.py
│   │   ├── jit.py
│   │   ├── parser_generics.py
│   │   ├── parser_pattern_matching.py
│   │   └── ssa_optimizer.py
│   │
│   ├── runtime/
│   │   └── gc.py
│   │
│   ├── stdlib/
│   │   ├── io.py
│   │   ├── math.py
│   │   ├── strings.py
│   │   ├── collections.py
│   │   ├── fs.py
│   │   ├── jsonlib.py
│   │   ├── time.py
│   │   └── system.py
│   │
│   ├── vm/
│   │   └── bytecode.py
│   │
│   ├── lsp/
│   │   └── server.py
│   │
│   ├── package_registry/
│   │   ├── client.py
│   │   └── server.py
│   │
│   ├── tools/
│   │   └── debugger.py
│   │
│   └── cli.py
│
├── examples/
│   ├── hello.pyx
│   ├── functions.pyx
│   └── conditions.pyx
│
├── tests/
│   ├── test_lexer_parser.py
│   ├── test_interpreter.py
│   └── test_vm.py
│
├── docs/
│   ├── README.md
│   ├── architecture.md
│   ├── cli.md
│   ├── stdlib.md
│   └── verification.md
│
├── pyx.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── BRANDING.md
├── INSTALL.md
├── GETTING_STARTED.md
├── CONTRIBUTING.md
├── STDLIB.md
├── REFERENCE.md
└── LICENSE
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/download.svg?color=%2322c55e" width="28" />
  Instalação
</h2>

Clone o repositório:

~~~bash
git clone https://github.com/lipeedeveloper/pyxcore.git
cd pyxcore
~~~

Instale em modo desenvolvimento:

~~~bash
pip install -e .
~~~

Instale com dependências extras opcionais:

~~~bash
pip install -e ".[llvm,server,dev]"
~~~

As dependências extras são:

- `llvm`: suporte experimental a LLVM e JIT com `llvmlite`;
- `server`: suporte ao registry local com FastAPI;
- `dev`: ferramentas para testes.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/terminal.svg?color=%23f97316" width="28" />
  CLI
</h2>

Executar arquivo `.pyx`:

~~~bash
pyx run examples/hello.pyx
~~~

Mostrar tokens:

~~~bash
pyx tokens examples/hello.pyx
~~~

Mostrar AST:

~~~bash
pyx ast examples/hello.pyx
~~~

Formatar arquivo:

~~~bash
pyx fmt examples/hello.pyx
~~~

Executar testes:

~~~bash
pyx test
~~~

Executar VM de exemplo:

~~~bash
pyx vm 2 3
~~~

Executar JIT experimental:

~~~bash
pyx jit --return-value 7
~~~

Publicar pacote no registry local:

~~~bash
pyx publish meu-pacote --version 0.1.0
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/library-books.svg?color=%236366f1" width="28" />
  Biblioteca padrão
</h2>

A biblioteca padrão atual é implementada em Python e fica em:

~~~txt
pyxcore/stdlib/
~~~

Módulos disponíveis:

### <img src="https://api.iconify.design/material-symbols/print.svg?color=%2322c55e" width="22" /> IO

Funções básicas de entrada e saída.

~~~python
println("Mensagem")
readln("Digite algo: ")
~~~

### <img src="https://api.iconify.design/material-symbols/functions.svg?color=%23f97316" width="22" /> Math

Funções e constantes matemáticas básicas.

~~~python
square(4)
cube(3)
clamp(10, 0, 5)
~~~

### <img src="https://api.iconify.design/material-symbols/text-fields.svg?color=%236366f1" width="22" /> Strings

Funções para manipulação de texto.

~~~python
upper("pyxcore")
lower("PYXCORE")
trim("  texto  ")
~~~

### <img src="https://api.iconify.design/material-symbols/table-rows.svg?color=%23a855f7" width="22" /> Collections

Funções auxiliares para listas e coleções.

~~~python
length([1, 2, 3])
first([1, 2, 3])
last([1, 2, 3])
~~~

### <img src="https://api.iconify.design/material-symbols/folder-open.svg?color=%23facc15" width="22" /> FS

Funções básicas para arquivos.

~~~python
read("arquivo.txt")
write("arquivo.txt", "conteúdo")
exists("arquivo.txt")
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/developer-mode.svg?color=%23a855f7" width="28" />
  Ferramentas de desenvolvimento
</h2>

### <img src="https://api.iconify.design/material-symbols/edit-note.svg?color=%236366f1" width="22" /> LSP experimental

O projeto possui um servidor LSP experimental com:

- autocomplete básico;
- diagnósticos simples;
- hover para símbolos conhecidos.

### <img src="https://api.iconify.design/material-symbols/bug-report.svg?color=%23ef4444" width="22" /> Debugger experimental

O debugger atual permite registrar breakpoints e eventos de execução. A integração completa com a VM ainda está em desenvolvimento.

### <img src="https://api.iconify.design/material-symbols/format-align-left.svg?color=%2306b6d4" width="22" /> Formatador

O formatador aplica indentação simples em arquivos `.pyx`.

~~~bash
pyx fmt examples/hello.pyx
~~~

### <img src="https://api.iconify.design/material-symbols/science.svg?color=%2322c55e" width="22" /> Test runner

O test runner executa os testes do projeto.

~~~bash
pyx test
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/inventory-2.svg?color=%23f97316" width="28" />
  Package registry experimental
</h2>

A PyxCore inclui um registry local experimental usando FastAPI.

Instale as dependências:

~~~bash
pip install -e ".[server]"
~~~

Inicie o registry:

~~~bash
uvicorn pyxcore.package_registry.server:app --reload
~~~

Publique um pacote:

~~~bash
pyx publish meu-pacote --version 0.1.0
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/speed.svg?color=%23facc15" width="28" />
  LLVM e JIT experimental
</h2>

A PyxCore possui um backend LLVM experimental usando `llvmlite`.

Instale as dependências:

~~~bash
pip install -e ".[llvm]"
~~~

Execute a demonstração:

~~~bash
pyx jit --return-value 7
~~~

Esse recurso atualmente gera e executa uma função `main` simples que retorna um inteiro. A integração completa com a AST da linguagem ainda está em desenvolvimento.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/memory-alt.svg?color=%23ef4444" width="28" />
  Gerenciamento de memória
</h2>

O projeto inclui um garbage collector experimental em Python, baseado em uma simulação de mark-and-sweep.

Ele serve para estudo e evolução do runtime. Ainda não gerencia memória nativa de programas PyxCore.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/science.svg?color=%2322c55e" width="28" />
  Testes
</h2>

Executar testes pela CLI:

~~~bash
pyx test
~~~

Executar testes diretamente com Python:

~~~bash
python -m unittest discover tests
~~~

Testes principais:

~~~txt
tests/test_lexer_parser.py
tests/test_interpreter.py
tests/test_vm.py
~~~

---

<h2>
  <img src="https://api.iconify.design/material-symbols/construction.svg?color=%23f97316" width="28" />
  Roadmap
</h2>

### <img src="https://api.iconify.design/material-symbols/check-circle.svg?color=%2322c55e" width="22" /> Base atual

- [x] Estrutura de package Python;
- [x] CLI instalável;
- [x] Lexer;
- [x] Parser;
- [x] AST;
- [x] Interpretador inicial;
- [x] Análise semântica inicial;
- [x] VM de bytecode;
- [x] Biblioteca padrão base;
- [x] Test runner;
- [x] Formatador;
- [x] LSP experimental;
- [x] Registry local experimental;
- [x] Backend LLVM experimental;
- [x] JIT experimental;
- [x] Documentação local em Markdown.

### <img src="https://api.iconify.design/material-symbols/pending-actions.svg?color=%23facc15" width="22" /> Próximos passos

- [ ] Melhorar mensagens de erro;
- [ ] Expandir parser;
- [ ] Integrar imports e módulos ao parser principal;
- [ ] Criar sistema de tipos mais completo;
- [ ] Integrar AST ao backend LLVM;
- [ ] Expandir VM de bytecode;
- [ ] Conectar debugger com VM;
- [ ] Expandir biblioteca padrão;
- [ ] Criar package manager com lockfile;
- [ ] Expandir LSP;
- [ ] Aumentar cobertura de testes.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/menu-book.svg?color=%236366f1" width="28" />
  Documentação local
</h2>

A documentação do projeto fica dentro do próprio repositório.

~~~txt
docs/
├── README.md
├── architecture.md
├── cli.md
├── stdlib.md
└── verification.md
~~~

O projeto não inclui website ou documentação web nesta fase.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/school.svg?color=%23facc15" width="28" />
  Para quem é a PyxCore?
</h2>

A PyxCore é indicada para:

- pessoas que querem aprender sobre linguagens de programação;
- desenvolvedores interessados em compiladores;
- estudantes que querem estudar lexer, parser, AST, VM e runtime;
- criadores que desejam construir uma linguagem própria;
- programadores que gostam de projetos experimentais;
- pessoas que querem estudar geração de código, LLVM e JIT.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/compare-arrows.svg?color=%23f97316" width="28" />
  Inspiração
</h2>

A PyxCore pode se inspirar em conceitos de várias linguagens modernas, sem deixar de buscar uma identidade própria.

Algumas inspirações:

- simplicidade de Python;
- organização de Go;
- produtividade de JavaScript;
- segurança de Rust;
- performance de C;
- ferramentas modernas de TypeScript;
- compilação avançada com LLVM.

A ideia não é copiar uma linguagem existente, mas aprender com boas ideias e criar uma experiência própria.

---

<h2>
  <img src="https://api.iconify.design/material-symbols/groups.svg?color=%2306b6d4" width="28" />
  Contribuição
</h2>

Contribuições são bem-vindas.

Você pode ajudar com:

- correção de bugs;
- documentação;
- exemplos;
- testes;
- compilador;
- biblioteca padrão;
- CLI;
- ferramentas;
- design da linguagem.

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

Caso encontre algum erro, abra uma issue no repositório:

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
- versão da PyxCore;
- passos para reproduzir o erro.

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

Isso ajuda o projeto a crescer, mostra que existe interesse na linguagem e incentiva o desenvolvimento de novas funcionalidades.

---

<div align="center">

<h2>
  <img src="https://api.iconify.design/material-symbols/code.svg?color=%236366f1" width="28" />
  pyxcore.language
</h2>

<p>
  <strong>Uma linguagem simples na entrada, organizada na base e poderosa na evolução.</strong>
</p>

<br/>

<img src="https://img.shields.io/badge/made%20with-code-6366f1?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/built%20with-caf%C3%A9%20e%20persist%C3%AAncia-f97316?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/project-pyxcore-22c55e?style=for-the-badge&labelColor=000000" />

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:6366f1&height=120&section=footer" />

</div>
