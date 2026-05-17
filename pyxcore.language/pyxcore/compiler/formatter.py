def format_source(source):
    indent=0; out=[]
    for raw in source.splitlines():
        line=raw.strip()
        if not line: out.append(''); continue
        if line.startswith('}'): indent=max(0,indent-1)
        out.append('    '*indent+line)
        if line.endswith('{'): indent+=1
    return '\n'.join(out).rstrip()+'\n'
