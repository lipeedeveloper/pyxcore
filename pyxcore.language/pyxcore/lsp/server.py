class PyxLanguageServer:
    KEYWORDS=['fn','let','return','if','else','while','match','case','import']; BUILTINS=['print','println','len','int','float','str','bool']; TYPES=['int','float','str','bool','List<T>','Map<K,V>','Option<T>']
    def complete(self,prefix): return [{'label':x,'kind':'keyword'} for x in self.KEYWORDS+self.BUILTINS+self.TYPES if x.startswith(prefix)]
    def diagnostics(self,text): return [{'line':i,'message':'Invalid token `??`'} for i,l in enumerate(text.splitlines(),1) if '??' in l]
    def hover(self,symbol): return {'fn':'Declares a function.','let':'Declares a local variable.','match':'Pattern matching expression.','println':'Prints a value with newline.'}.get(symbol,'No documentation available.')
