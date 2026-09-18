import pandas as pd
from synergy_marketvision.core import *

def test_cube_shape():
    n=64;f=pd.DataFrame({'open':range(1,n+1),'high':range(2,n+2),'low':range(n),'close':range(1,n+1),'volume':[100]*n})
    c=market_cube(f,64);assert c.shape==(3,64,4)
