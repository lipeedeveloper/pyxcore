class PatternMatchParser:
    def parse_match(self,text):
        lines=[l.strip() for l in text.splitlines() if l.strip()]
        if not lines or not lines[0].startswith('match '): raise SyntaxError('Expected match')
        subject=lines[0][len('match '):].rstrip(':').strip(); cases=[]
        for line in lines[1:]:
            if not line.startswith('case ') or '=>' not in line: raise SyntaxError(f'Invalid case: {line}')
            a,b=line[len('case '):].split('=>',1); cases.append({'pattern':a.strip(),'body':b.strip()})
        return {'type':'match','subject':subject,'cases':cases}
