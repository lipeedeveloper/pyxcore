@echo off
setlocal EnableExtensions
title PyxCore Compiler Installer
set "PS_EXE="
if exist "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" set "PS_EXE=%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe"
if not defined PS_EXE if exist "%SystemRoot%\Sysnative\WindowsPowerShell\v1.0\powershell.exe" set "PS_EXE=%SystemRoot%\Sysnative\WindowsPowerShell\v1.0\powershell.exe"
if not defined PS_EXE (
  echo [ERRO] PowerShell nao encontrado.
  pause
  exit /b 1
)
"%PS_EXE%" -NoProfile -ExecutionPolicy Bypass -File "%~dp0install_pyxcore.ps1"
pause
