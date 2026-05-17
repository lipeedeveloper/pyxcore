# Guia de Instalação

## Pré-requisitos

- **Python** 3.7 ou superior
- **Compilador C** (gcc, clang ou MSVC)

## Configuração por Plataforma

### Linux (Ubuntu/Debian)

```bash
# Instale as ferramentas necessárias
sudo apt update
sudo apt install build-essential python3 python3-pip

# Clone o PyxCore
git clone https://github.com/lipeedeveloper/pyxcore.git
cd pyxcore

# Torne o pyxc executável
chmod +x compiler/pyxc.py

# Adicione ao PATH (opcional)
echo "export PATH=\"\$PATH:$(pwd)/compiler\"" >> ~/.bashrc
source ~/.bashrc

# Verifique a instalação
python3 compiler/pyxc.py --version
```

### macOS

```bash
# Instale as ferramentas de linha de comando do Xcode
xcode-select --install

# Instale o Homebrew (se não estiver instalado)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Clone o PyxCore
git clone https://github.com/lipeedeveloper/pyxcore.git
cd pyxcore

# Torne o pyxc executável
chmod +x compiler/pyxc.py

# Adicione ao PATH
echo "export PATH=\"\$PATH:$(pwd)/compiler\"" >> ~/.zprofile
source ~/.zprofile

# Verifique a instalação
python3 compiler/pyxc.py --version
```

### Windows

#### Opção 1: Usando MinGW

```cmd
# Instale o MinGW em https://www.mingw-w64.org/

# Clone o PyxCore
git clone https://github.com/lipeedeveloper/pyxcore.git
cd pyxcore

# Crie um script em lote (pyxc.bat)
echo @python.exe "%~dp0compiler\pyxc.py" %* > pyxc.bat

# Adicione ao PATH (Propriedades do Sistema > Variáveis de Ambiente)
# Adicione o diretório que contém pyxc.bat ao PATH

# Verifique a instalação
pyxc --version
```

#### Opção 2: Usando MSVC (Visual Studio)

```cmd
# Instale o Visual Studio ou Visual Studio Build Tools
# Selecione "Desktop development with C++"

# Clone o PyxCore
git clone https://github.com/lipeedeveloper/pyxcore.git
cd pyxcore

# Crie um script em lote (pyxc.bat)
echo @python.exe "%~dp0compiler\pyxc.py" %* > pyxc.bat

# Adicione o diretório atual ao PATH ou ao PATH do sistema

# Verifique a instalação
pyxc --version
```

## Verificando a Instalação

```bash
# Verifique o Python
python --version          # Deve ser 3.7+

# Verifique o compilador C
gcc --version            # ou clang --version

# Verifique o compilador PyxCore
pyxc --version          # Deve mostrar v2.0.0

# Teste a compilação
echo 'fn main() { print("Olá!") }' > test.pyx
pyxc test.pyx
./test                   # ./test.exe no Windows
```

## Solução de Problemas

### "Python não encontrado"

```bash
# Use python3 explicitamente
python3 compiler/pyxc.py hello.pyx

# Ou crie um alias
alias pyxc='python3 /path/to/pyxcore/compiler/pyxc.py'
```

### "Compilador C não encontrado"

Instale gcc ou clang:

```bash
# Ubuntu/Debian
sudo apt install build-essential

# macOS
xcode-select --install

# Windows (MinGW)
# Baixe em https://www.mingw-w64.org/
```


## Próximos Passos

- Leia [GETTING_STARTED.md](GETTING_STARTED.md) para aprender os fundamentos da linguagem
- Confira [examples/](examples/) para exemplos de código
- Comece a usar a linguagem completa construída sobre a base de PyxCore

## Suporte

- **GitHub Issues**: https://github.com/lipeedeveloper/pyxcore/issues


---

**Developed Emanuel Felipe - Lipe Developer**

*PyxCore é a base da linguagem e oferece uma implementação completa para criação de código seguro e eficiente.*