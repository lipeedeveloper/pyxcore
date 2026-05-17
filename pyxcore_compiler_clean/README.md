# PyxCore Compiler

Versão limpa do PyxCore sem IA, sem Groq e sem comandos `ask`.

## Recursos

- Lexer
- Parser
- AST
- Análise semântica
- Runtime interpretado
- Bytecode VM simples
- Formatter
- Test runner
- CLI `pyx`
- Instalador Windows
- Exemplos `.pyx`

## Instalar no Windows

Abra:

```txt
install_pyxcore.cmd
```

Depois feche e abra o terminal.

## Comandos

```bash
pyx doctor
pyx --version
pyx new meu_app
pyx run main.pyx
pyx check main.pyx
pyx tokens main.pyx
pyx ast main.pyx
pyx fmt main.pyx
pyx repl
pyx test
```

## Exemplo

```pyx
fn main() {
    println("Bem-vindo ao PyxCore!")
    let nome = "Mundo"
    println("Olá, " + nome + "!")
}
```

Rodar:

```bash
pyx run examples/hello.pyx
```
