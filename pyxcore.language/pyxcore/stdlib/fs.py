from pathlib import Path
def read(path): return Path(path).read_text(encoding='utf-8')
def write(path,content): Path(path).write_text(str(content),encoding='utf-8')
def exists(path): return Path(path).exists()
