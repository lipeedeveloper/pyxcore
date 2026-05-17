import json
from urllib.request import Request, urlopen
class RegistryClient:
    def __init__(self,base_url='http://127.0.0.1:8000'): self.base_url=base_url.rstrip('/')
    def list_packages(self): return self._get('/packages')
    def publish(self,name,version,description='',author=''):
        payload=json.dumps({'name':name,'version':version,'description':description,'author':author}).encode('utf-8')
        req=Request(self.base_url+'/publish',data=payload,headers={'Content-Type':'application/json'},method='POST')
        with urlopen(req) as resp: return json.loads(resp.read().decode('utf-8'))
    def _get(self,path):
        with urlopen(self.base_url+path) as resp: return json.loads(resp.read().decode('utf-8'))
