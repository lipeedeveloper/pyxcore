from dataclasses import dataclass, field
@dataclass
class GCObject: value:object; marked:bool=False; refs:list=field(default_factory=list)
class GarbageCollector:
    def __init__(self): self.objects=[]; self.roots=[]
    def alloc(self,value): obj=GCObject(value); self.objects.append(obj); return obj
    def add_root(self,obj):
        if obj not in self.roots: self.roots.append(obj)
    def remove_root(self,obj):
        if obj in self.roots: self.roots.remove(obj)
    def collect(self):
        for o in self.objects: o.marked=False
        for r in self.roots: self.mark(r)
        before=len(self.objects); self.objects=[o for o in self.objects if o.marked]; return {'before':before,'after':len(self.objects),'collected':before-len(self.objects)}
    def mark(self,obj):
        if obj.marked: return
        obj.marked=True
        for r in obj.refs: self.mark(r)
