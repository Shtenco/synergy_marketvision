from __future__ import annotations
from typing import Any
import pandas as pd

from .core import market_cube, summary_features

CONTRACT_ID = "synergy.trading.market-features/v1"
AUTHORITY = "market_perception"


def market_features_payload(
    *,
    symbol: str,
    bars: list[dict[str, float]],
    window: int = 64,
    observation_id: str,
) -> dict[str, Any]:
    if not symbol.strip():
        raise ValueError("symbol required")
    if not observation_id.strip():
        raise ValueError("observation_id required")
    cube = market_cube(pd.DataFrame(bars), window)
    features = summary_features(cube)
    return {
        "observation_id": observation_id,
        "symbol": symbol.upper(),
        "window": int(window),
        "features": features,
        "authorization": False,
    }
