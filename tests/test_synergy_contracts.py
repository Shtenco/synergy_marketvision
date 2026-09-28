from synergy_marketvision.synergy_contracts import CONTRACT_ID, market_features_payload

def test_market_features_payload_is_advisory():
    bars=[{"open":1+i*.001,"high":1.01+i*.001,"low":.99+i*.001,"close":1.0+i*.001,"volume":100+i} for i in range(64)]
    p=market_features_payload(symbol="eurusd",bars=bars,window=64,observation_id="obs-1")
    assert CONTRACT_ID=="synergy.trading.market-features/v1"
    assert p["symbol"]=="EURUSD"
    assert p["features"]["shape"]==[3,64,4]
    assert p["authorization"] is False
