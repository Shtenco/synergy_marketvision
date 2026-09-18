from __future__ import annotations
import pandas as pd
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..core import market_cube, summary_features
from .models import Principal, Role
from .service import EnterpriseRuntime, principal_dependency, request_id_header

class Bar(BaseModel): open:float; high:float; low:float; close:float; volume:float
class FeatureRequest(BaseModel): bars:list[Bar]; window:int=64

def build_product_router(runtime:EnterpriseRuntime)->APIRouter:
    router=APIRouter(prefix="/enterprise/v1/marketvision",tags=["enterprise-marketvision"])
    @router.post("/features")
    async def features(req:FeatureRequest, principal:Principal=Depends(principal_dependency(runtime,{Role.RESEARCHER,Role.TRADER})), request_id:str=Depends(request_id_header)):
        frame=pd.DataFrame([b.model_dump() for b in req.bars]);cube=market_cube(frame,window=req.window);summary=summary_features(cube)
        runtime.record(principal,action="marketvision.features",request_id=request_id,payload={"window":req.window,"shape":summary["shape"],"energy":summary["energy"]})
        return {"request_id":request_id,**summary}
    return router
