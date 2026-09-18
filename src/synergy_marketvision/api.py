from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd,uvicorn
from .core import market_cube,summary_features
app=FastAPI(title='SYNERGY MarketVision',version='2.0.0')
class Bar(BaseModel):open:float;high:float;low:float;close:float;volume:float
class Req(BaseModel):bars:list[Bar];window:int=64
@app.get('/health')
def health():return {'ok':True,'service':'marketvision'}
@app.post('/v1/features')
def features(req:Req):
    cube=market_cube(pd.DataFrame([b.model_dump() for b in req.bars]),req.window);return summary_features(cube)

# Enterprise v2 control/data plane
from .enterprise.service import EnterpriseRuntime, build_enterprise_router, install_observability
from .enterprise.product import build_product_router
enterprise_runtime=EnterpriseRuntime.from_env(service_name='synergy-marketvision')
install_observability(app,enterprise_runtime)
app.include_router(build_enterprise_router(enterprise_runtime))
app.include_router(build_product_router(enterprise_runtime))

if __name__=='__main__':uvicorn.run(app,host='0.0.0.0',port=8000)
