<div align="center">
  <img height="200" src="https://i.ibb.co/qMYNww1G/rounded-in-photoretrica-1.png" />
</div>

###

<h1 align="center">pyxcore.language</h1>

###

<div align="center">
  <p>
    <strong>Uma linguagem de programação moderna, expressiva e poderosa, criada para transformar ideias, café e persistência em sistemas reais.</strong>
  </p>
</div>

###

<div align="center">

<img src="https://img.shields.io/badge/status-em%20desenvolvimento-111827?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/language-pyxcore-6366f1?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/compiler-pyx%20compiler-22c55e?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/runtime-python%20vm-f97316?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/focus-tooling-06b6d4?style=for-the-badge&labelColor=000000" />

</div>

###

<div align="center">
  <p>
    <img src="https://api.iconify.design/material-symbols/code.svg?color=%236366f1" width="20" />
    Simples para começar.
    <img src="https://api.iconify.design/material-symbols/bolt.svg?color=%23facc15" width="20" />
    Estruturada para crescer.
    <img src="https://api.iconify.design/material-symbols/rocket-launch.svg?color=%2322c55e" width="20" />
    Projetada para evoluir.
  </p>
</div>

---

<h2><img src="https://api.iconify.design/material-symbols/info.svg?color=%236366f1" width="28" /> Sobre a PyxCore</h2>

**PyxCore** é uma linguagem de programação em desenvolvimento com foco em clareza, organização e estudo de compiladores.

Este repositório contém uma implementação funcional inicial do ecossistema PyxCore, incluindo lexer, parser, AST, analisador semântico, VM de bytecode, runtime experimental, biblioteca padrão em Python, CLI, ferramentas de desenvolvimento, testes e documentação.

A PyxCore ainda não deve ser tratada como uma linguagem pronta para produção. Ela é uma base real de desenvolvimento, feita para evoluir de forma organizada até chegar a recursos mais avançados como geração nativa, LLVM, JIT, módulos completos, package registry e integração profunda com editores.

---

<h2><img src="https://api.iconify.design/material-symbols/checklist.svg?color=%2322c55e" width="28" /> Estado real do projeto</h2>

### <img src="https://api.iconify.design/material-symbols/check-circle.svg?color=%2322c55e" width="22" /> Implementado

- Lexer funcional para tokens básicos da linguagem;
- Parser funcional para funções, variáveis, chamadas, blocos, condições, loops e retornos;
- AST com nós estruturados;
- Analisador semântico inicial com escopos e símbolos;
- Interpretador simples para executar AST;
- VM de bytecode baseada em stack;
- Biblioteca padrão em Python;
- CLI com comandos reais;
- Test runner;
- Formatador simples;
- LSP experimental com autocomplete, hover e diagnósticos básicos;
- Package registry local com FastAPI quando dependências extras estiverem instaladas;
- Backend LLVM experimental usando `llvmlite` quando disponível;
- JIT experimental usando `llvmlite` quando disponível;
- Instalação via `pip install -e .`.

### <img src="https://api.iconify.design/material-symbols/pending-actions.svg?color=%23facc15" width="22" /> Experimental

- LLVM backend;
- JIT;
- Garbage collector;
- Package registry;
- LSP;
- Pattern matching;
- Generics;
- Otimizações SSA.

Essas partes existem como módulos reais e testáveis, mas ainda são bases de evolução. Elas não representam uma implementação completa de linguagem de produção.

---

<h2><img src="https://api.iconify.design/material-symbols/code-blocks.svg?color=%236366f1" width="28" /> Exemplo de código</h2>

~~~pyx
fn main() {
    print("Olá, PyxCore!")

    let nome = "Developer"
    print("Bem-vindo, " + nome)
}
~~~

~~~pyx
fn soma(a, b) {
    return a + b
}

fn main() {
    let resultado = soma(10, 20)
    print(resultado)
}
~~~

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

---

<h2><img src="https://api.iconify.design/material-symbols/account-tree.svg?color=%2306b6d4" width="28" /> Como a PyxCore funciona</h2>

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
Execução por AST ou Bytecode VM
    ↓
Runtime / Stdlib
~~~

A implementação atual prioriza uma base clara e testável. O compilador transforma código `.pyx` em tokens, depois em AST, executa validações semânticas e permite execução por interpretador ou por VM experimental.

---

<h2><img src="https://api.iconify.design/material-symbols/folder.svg?color=%23facc15" width="28" /> Estrutura do projeto</h2>

~~~txt
pyxcore/
├── pyxcore/
│   ├── compiler/
│   ├── runtime/
│   ├── stdlib/
│   ├── vm/
│   ├── lsp/
│   ├── package_registry/
│   └── cli.py
├── examples/
├── tests/
├── docs/
├── ├── pyproject.toml
└── README.md
~~~

---

<h2><img src="https://api.iconify.design/material-symbols/download.svg?color=%2322c55e" width="28" /> Instalação</h2>

~~~bash
pip install -e .
~~~

~~~bash
pip install -e ".[llvm,server,dev]"
~~~

As dependências extras são opcionais:

- `llvm`: habilita backend LLVM e JIT experimental com `llvmlite`;
- `server`: habilita package registry local com FastAPI;
- `dev`: instala ferramentas para testes.

---

<h2><img src="https://api.iconify.design/material-symbols/terminal.svg?color=%23f97316" width="28" /> CLI</h2>

~~~bash
pyx run examples/hello.pyx
pyx tokens examples/hello.pyx
pyx ast examples/hello.pyx
pyx fmt examples/hello.pyx
pyx test
pyx vm 2 3
pyx jit --return-value 7
pyx publish meu-pacote --version 0.1.0
~~~

---

<h2><img src="https://api.iconify.design/material-symbols/library-books.svg?color=%236366f1" width="28" /> Biblioteca padrão</h2>

A biblioteca padrão atual fica em `pyxcore/stdlib/` e contém módulos em Python que servem como base para recursos internos da linguagem.

~~~txt
stdlib/
├── io.py
├── math.py
├── strings.py
├── collections.py
├── fs.py
├── jsonlib.py
├── time.py
└── system.py
~~~

---

<h2><img src="https://api.iconify.design/material-symbols/hub.svg?color=%2322c55e" width="28" /> Recursos da linguagem</h2>

### <img src="https://api.iconify.design/material-symbols/variable-add.svg?color=%2322c55e" width="22" /> Variáveis

~~~pyx
let nome = "PyxCore"
let versao = 1
~~~

### <img src="https://api.iconify.design/material-symbols/function.svg?color=%23f97316" width="22" /> Funções

~~~pyx
fn multiplicar(a, b) {
    return a * b
}
~~~

### <img src="https://api.iconify.design/material-symbols/alt-route.svg?color=%23facc15" width="22" /> Condicionais

~~~pyx
if ativo {
    print("Sistema ativo")
} else {
    print("Sistema inativo")
}
~~~

### <img src="https://api.iconify.design/material-symbols/repeat.svg?color=%2306b6d4" width="22" /> Loops

~~~pyx
while contador < 10 {
    print(contador)
    contador = contador + 1
}
~~~

### <img src="https://api.iconify.design/material-symbols/join-inner.svg?color=%23f97316" width="22" /> Pattern matching experimental

O parser auxiliar de pattern matching existe como módulo experimental. A sintaxe ainda está em evolução.

### <img src="https://api.iconify.design/material-symbols/category.svg?color=%23ec4899" width="22" /> Generics experimental

O parser auxiliar de generics existe para analisar assinaturas como `List<int>` e `Map<string, int>`. O sistema de tipos completo ainda está em desenvolvimento.

---

<h2><img src="https://api.iconify.design/material-symbols/speed.svg?color=%23facc15" width="28" /> LLVM e JIT</h2>

O backend LLVM usa `llvmlite` quando a dependência extra está instalada.

~~~bash
pip install -e ".[llvm]"
pyx jit --return-value 7
~~~

Esse recurso atualmente gera uma função `main` simples que retorna um inteiro. A integração completa do AST da linguagem com LLVM ainda está em desenvolvimento.

---

<h2><img src="https://api.iconify.design/material-symbols/inventory-2.svg?color=%23f97316" width="28" /> Package registry</h2>

Iniciar servidor local:

~~~bash
uvicorn pyxcore.package_registry.server:app --reload
~~~

Publicar pacote:

~~~bash
pyx publish meu-pacote --version 0.1.0
~~~

---

<h2><img src="https://api.iconify.design/material-symbols/science.svg?color=%2322c55e" width="28" /> Testes</h2>

~~~bash
pyx test
python -m unittest discover tests
~~~

---

<h2><img src="https://api.iconify.design/material-symbols/construction.svg?color=%23f97316" width="28" /> Roadmap</h2>

### <img src="https://api.iconify.design/material-symbols/check-circle.svg?color=%2322c55e" width="22" /> Base atual

- [x] Estrutura de package Python;
- [x] CLI instalável;
- [x] Lexer;
- [x] Parser;
- [x] AST;
- [x] Interpretador inicial;
- [x] Semantic analyzer inicial;
- [x] VM de bytecode;
- [x] Stdlib base;
- [x] Test runner;
- [x] Formatador;
- [x] LSP experimental;
- [x] Registry local experimental;
- [x] Backend LLVM experimental;
- [x] JIT experimental;
- [x] Documentação padronizada.

### <img src="https://api.iconify.design/material-symbols/pending-actions.svg?color=%23facc15" width="22" /> Próximos passos reais

- [ ] Integrar AST completo com LLVM;
- [ ] Expandir sistema de tipos;
- [ ] Implementar módulos/imports no parser principal;
- [ ] Conectar GC ao runtime real;
- [ ] Expandir LSP para protocolo completo;
- [ ] Criar package resolver com lockfile;
- [ ] Criar debugger integrado com VM;
- [ ] Expandir stdlib em `.pyx`;
- [ ] Adicionar suíte de testes maior;
- [ ] 
---

<h2><img src="https://api.iconify.design/material-symbols/groups.svg?color=%2306b6d4" width="28" /> Contribuição</h2>

~~~bash
git checkout -b minha-feature
git add .
git commit -m "feat: adiciona nova funcionalidade"
git push origin minha-feature
~~~

---

<h2><img src="https://api.iconify.design/material-symbols/bug-report.svg?color=%23ef4444" width="28" /> Reportar problemas</h2>

Inclua descrição do problema, código que causou o erro, mensagem recebida, comportamento esperado, sistema operacional, versão do Python, versão da PyxCore e passos para reproduzir.

---

<h2><img src="https://api.iconify.design/material-symbols/security.svg?color=%2322c55e" width="28" /> Licença</h2>

Este projeto pode ser distribuído sob a licença MIT.

---

<div align="center">

<h2><img src="https://api.iconify.design/material-symbols/code.svg?color=%236366f1" width="28" /> pyxcore.language</h2>

<p><strong>Uma linguagem simples na entrada, organizada na base e poderosa na evolução.</strong></p>

<br/>

<img src="https://img.shields.io/badge/made%20with-code-6366f1?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/built%20with-caf%C3%A9%20e%20persist%C3%AAncia-f97316?style=for-the-badge&labelColor=000000" />
<img src="https://img.shields.io/badge/project-pyxcore-22c55e?style=for-the-badge&labelColor=000000" />

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:6366f1&height=120&section=footer" />

</div>
