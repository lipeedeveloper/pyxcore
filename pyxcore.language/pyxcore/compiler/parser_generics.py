class GenericParser:
    def parse_generic(self,text):
        text=text.strip()
        if '<' not in text or not text.endswith('>'): return {'base':text,'params':[]}
        return {'base':text[:text.find('<')].strip(),'params':[p.strip() for p in text[text.find('<')+1:-1].split(',') if p.strip()]}
