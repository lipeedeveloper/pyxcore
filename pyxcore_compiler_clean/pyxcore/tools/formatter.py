def format_source(source):
    indent=0; lines=[]
    for raw in source.splitlines():
        line=raw.strip()
        if not line: lines.append(""); continue
        if line.startswith("}"): indent=max(0,indent-1)
        lines.append("    "*indent+line)
        if line.endswith("{"): indent+=1
    return "\n".join(lines).rstrip()+"\n"
