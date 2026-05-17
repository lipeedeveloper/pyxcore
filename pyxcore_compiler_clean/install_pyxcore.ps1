$ErrorActionPreference = "Stop"
$InstallRoot = Join-Path $env:LOCALAPPDATA "PyxCoreCompiler"
$Source = Join-Path $InstallRoot "source"
$Venv = Join-Path $InstallRoot ".venv"
$Bin = Join-Path $InstallRoot "bin"
function Step($m){Write-Host "";Write-Host "==> $m" -ForegroundColor Cyan}
function Ok($m){Write-Host "[OK] $m" -ForegroundColor Green}
function Fail($m){Write-Host "[ERRO] $m" -ForegroundColor Red; exit 1}
Step "Verificando Python"
$PythonCmd=$null
if(Get-Command py -ErrorAction SilentlyContinue){try{& py -3 --version|Out-Null;$PythonCmd="py"}catch{}}
if(-not $PythonCmd -and (Get-Command python -ErrorAction SilentlyContinue)){try{& python --version|Out-Null;$PythonCmd="python"}catch{}}
if(-not $PythonCmd){Fail "Python 3 nao encontrado."}
Step "Copiando arquivos"
New-Item -ItemType Directory -Force -Path $Source | Out-Null
New-Item -ItemType Directory -Force -Path $Bin | Out-Null
Remove-Item $Source -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force -Path $Source | Out-Null
Copy-Item "$PSScriptRoot\pyxcore" $Source -Recurse -Force
Copy-Item "$PSScriptRoot\pyproject.toml" $Source -Force
Copy-Item "$PSScriptRoot\README.md" $Source -Force
Copy-Item "$PSScriptRoot\examples" $Source -Recurse -Force
Copy-Item "$PSScriptRoot\tests" $Source -Recurse -Force
Step "Criando venv"
Remove-Item $Venv -Recurse -Force -ErrorAction SilentlyContinue
if($PythonCmd -eq "py"){& py -3 -m venv $Venv}else{& python -m venv $Venv}
$VenvPython=Join-Path $Venv "Scripts\python.exe"
$VenvPip=Join-Path $Venv "Scripts\pip.exe"
Step "Instalando"
& $VenvPython -m pip install --upgrade pip setuptools wheel
& $VenvPip install -e $Source
if($LASTEXITCODE -ne 0){Fail "pip install falhou"}
Step "Criando comando pyx"
$Launcher=Join-Path $Bin "pyx_launcher.py"
Set-Content -Path $Launcher -Encoding UTF8 -Value @"
import os, sys
SOURCE = r"$Source"
CWD = os.getcwd()
sys.path[:] = [SOURCE] + [p for p in sys.path if p not in ("", CWD)]
from pyxcore.cli import main
raise SystemExit(main())
"@
$Cmd=Join-Path $Bin "pyx.cmd"
Set-Content -Path $Cmd -Encoding ASCII -Value "@echo off`r`n`"$VenvPython`" `"$Launcher`" %*`r`n"
$current=[Environment]::GetEnvironmentVariable("Path","User")
if($null -eq $current){$current=""}
$parts=$current -split ";" | Where-Object {$_ -ne ""}
if($parts -notcontains $Bin){[Environment]::SetEnvironmentVariable("Path","$current;$Bin","User");$env:Path="$env:Path;$Bin"}
Step "Testando"
& $Cmd doctor
& $Cmd run (Join-Path $Source "examples\hello.pyx")
Ok "PyxCore Compiler instalado. Feche e abra o terminal e rode: pyx doctor"
