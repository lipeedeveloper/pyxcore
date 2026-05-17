@echo off
setlocal
set "PS_EXE=%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe"
"%PS_EXE%" -NoProfile -ExecutionPolicy Bypass -Command "$p=Join-Path $env:LOCALAPPDATA 'PyxCoreCompiler'; $b=Join-Path $p 'bin'; if(Test-Path $p){Remove-Item $p -Recurse -Force}; $old=[Environment]::GetEnvironmentVariable('Path','User'); if($old){$parts=$old -split ';' | ? {$_ -and $_ -ne $b}; [Environment]::SetEnvironmentVariable('Path',($parts -join ';'),'User')}; Write-Host 'PyxCore removido.'"
pause
