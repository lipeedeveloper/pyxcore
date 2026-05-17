from pathlib import Path
from pyxcore.compiler.pipeline import run_source
def run_tests(path="tests"):
    root=Path(path)
    if not root.exists(): print(f"pasta de testes não encontrada: {root}"); return 1
    files=sorted(root.rglob("*.pyx"))
    failed=0
    for file in files:
        try: run_source(file.read_text(encoding="utf-8"),str(file)); print(f"OK {file}")
        except Exception as exc: failed+=1; print(f"FAIL {file}: {exc}")
    print(f"{len(files)-failed}/{len(files)} testes passaram")
    return 1 if failed else 0
