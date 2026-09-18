from __future__ import annotations
import numpy as np
import pandas as pd

REQ=('open','high','low','close','volume')

def robust_scale(x:np.ndarray)->np.ndarray:
    med=np.nanmedian(x,axis=0);q1=np.nanquantile(x,.25,axis=0);q3=np.nanquantile(x,.75,axis=0);iqr=np.where((q3-q1)==0,1,q3-q1)
    return (x-med)/iqr

def market_cube(frame:pd.DataFrame,window:int=64)->np.ndarray:
    missing=[c for c in REQ if c not in frame]
    if missing:raise ValueError(f'missing columns: {missing}')
    f=frame.tail(window).copy()
    if len(f)<window:raise ValueError('not enough rows')
    close=f['close'].to_numpy(float);ret=np.r_[0,np.diff(np.log(np.maximum(close,1e-12)))]
    spread=((f['high']-f['low'])/np.maximum(f['close'].abs(),1e-12)).to_numpy(float)
    vol=f['volume'].to_numpy(float)
    direction=np.sign(ret)
    data=np.column_stack([ret,spread,np.log1p(np.maximum(vol,0)),direction])
    scaled=robust_scale(data)
    # channels x time x feature; first two channels preserve signed and absolute structure
    return np.stack([scaled, np.abs(scaled), np.sign(scaled)],axis=0).astype('float32')

def summary_features(cube:np.ndarray)->dict:
    return {'shape':list(cube.shape),'mean':float(cube.mean()),'std':float(cube.std()),'energy':float(np.mean(cube**2))}
