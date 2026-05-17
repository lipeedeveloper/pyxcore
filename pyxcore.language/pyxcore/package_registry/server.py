from pathlib import Path
from typing import Optional
import json, time
try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
except Exception:
    FastAPI=None; BaseModel=object; HTTPException=Exception
REGISTRY_DIR=Path.home()/'.pyxcore'/'registry'; REGISTRY_FILE=REGISTRY_DIR/'packages.json'
def _load():
    REGISTRY_DIR.mkdir(parents=True,exist_ok=True)
    if not REGISTRY_FILE.exists(): REGISTRY_FILE.write_text('{}',encoding='utf-8')
    return json.loads(REGISTRY_FILE.read_text(encoding='utf-8'))
def _save(data): REGISTRY_DIR.mkdir(parents=True,exist_ok=True); REGISTRY_FILE.write_text(json.dumps(data,indent=2),encoding='utf-8')
if FastAPI:
    app=FastAPI(title='PyxCore Package Registry',version='0.1.0')
    class PublishRequest(BaseModel):
        name:str; version:str; description:str=''; author:str=''; tarball_url:Optional[str]=None
    @app.get('/')
    def root(): return {'name':'PyxCore Registry','status':'online'}
    @app.get('/packages')
    def packages(): return _load()
    @app.get('/packages/{name}')
    def package(name:str):
        data=_load()
        if name not in data: raise HTTPException(status_code=404,detail='Package not found')
        return data[name]
    @app.post('/publish')
    def publish(req:PublishRequest):
        data=_load(); versions=data.setdefault(req.name,{'versions':{}})['versions']; versions[req.version]={'description':req.description,'author':req.author,'tarball_url':req.tarball_url,'published_at':int(time.time())}; _save(data); return {'ok':True,'package':req.name,'version':req.version}
else: app=None
