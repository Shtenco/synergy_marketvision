import json
from fastapi.testclient import TestClient
from synergy_marketvision.api import app
from synergy_marketvision.enterprise.auth import sign_token
from synergy_marketvision.enterprise.models import Role

SECRET="dev-only-change-me-not-for-production"

def token(role):
    return sign_token(SECRET,subject="fund-user",roles=[Role(role)],tenant_id="fund-a",ttl_seconds=3600)

def test_product_enterprise_endpoint_and_audit_linkage():
    c=TestClient(app)
    request_id="acceptance-123"
    res=c.post('/enterprise/v1/marketvision/features',json={'window': 16, 'bars': [{'open': 100.0, 'high': 100.5, 'low': 99.5, 'close': 100.2, 'volume': 1000}, {'open': 100.1, 'high': 100.6, 'low': 99.6, 'close': 100.3, 'volume': 1010}, {'open': 100.2, 'high': 100.7, 'low': 99.7, 'close': 100.4, 'volume': 1020}, {'open': 100.3, 'high': 100.8, 'low': 99.8, 'close': 100.5, 'volume': 1030}, {'open': 100.4, 'high': 100.9, 'low': 99.9, 'close': 100.60000000000001, 'volume': 1040}, {'open': 100.5, 'high': 101.0, 'low': 100.0, 'close': 100.7, 'volume': 1050}, {'open': 100.6, 'high': 101.1, 'low': 100.1, 'close': 100.8, 'volume': 1060}, {'open': 100.7, 'high': 101.2, 'low': 100.2, 'close': 100.9, 'volume': 1070}, {'open': 100.8, 'high': 101.3, 'low': 100.3, 'close': 101.0, 'volume': 1080}, {'open': 100.9, 'high': 101.4, 'low': 100.4, 'close': 101.10000000000001, 'volume': 1090}, {'open': 101.0, 'high': 101.5, 'low': 100.5, 'close': 101.2, 'volume': 1100}, {'open': 101.1, 'high': 101.6, 'low': 100.6, 'close': 101.3, 'volume': 1110}, {'open': 101.2, 'high': 101.7, 'low': 100.7, 'close': 101.4, 'volume': 1120}, {'open': 101.3, 'high': 101.8, 'low': 100.8, 'close': 101.5, 'volume': 1130}, {'open': 101.4, 'high': 101.9, 'low': 100.9, 'close': 101.60000000000001, 'volume': 1140}, {'open': 101.5, 'high': 102.0, 'low': 101.0, 'close': 101.7, 'volume': 1150}, {'open': 101.6, 'high': 102.1, 'low': 101.1, 'close': 101.8, 'volume': 1160}, {'open': 101.7, 'high': 102.2, 'low': 101.2, 'close': 101.9, 'volume': 1170}, {'open': 101.8, 'high': 102.3, 'low': 101.3, 'close': 102.0, 'volume': 1180}, {'open': 101.9, 'high': 102.4, 'low': 101.4, 'close': 102.10000000000001, 'volume': 1190}]},headers={"Authorization":"Bearer "+token('researcher'),"X-Request-ID":request_id})
    assert res.status_code==200, res.text
    body=res.json()
    for key in ['shape', 'energy', 'request_id']: assert key in body
    assert body["request_id"]==request_id
    admin=token("admin")
    audit=c.get('/enterprise/audit',headers={"Authorization":"Bearer "+admin})
    assert audit.status_code==200
    assert any(e["request_id"]==request_id for e in audit.json())

def test_product_endpoint_requires_authorized_role():
    c=TestClient(app)
    res=c.post('/enterprise/v1/marketvision/features',json={'window': 16, 'bars': [{'open': 100.0, 'high': 100.5, 'low': 99.5, 'close': 100.2, 'volume': 1000}, {'open': 100.1, 'high': 100.6, 'low': 99.6, 'close': 100.3, 'volume': 1010}, {'open': 100.2, 'high': 100.7, 'low': 99.7, 'close': 100.4, 'volume': 1020}, {'open': 100.3, 'high': 100.8, 'low': 99.8, 'close': 100.5, 'volume': 1030}, {'open': 100.4, 'high': 100.9, 'low': 99.9, 'close': 100.60000000000001, 'volume': 1040}, {'open': 100.5, 'high': 101.0, 'low': 100.0, 'close': 100.7, 'volume': 1050}, {'open': 100.6, 'high': 101.1, 'low': 100.1, 'close': 100.8, 'volume': 1060}, {'open': 100.7, 'high': 101.2, 'low': 100.2, 'close': 100.9, 'volume': 1070}, {'open': 100.8, 'high': 101.3, 'low': 100.3, 'close': 101.0, 'volume': 1080}, {'open': 100.9, 'high': 101.4, 'low': 100.4, 'close': 101.10000000000001, 'volume': 1090}, {'open': 101.0, 'high': 101.5, 'low': 100.5, 'close': 101.2, 'volume': 1100}, {'open': 101.1, 'high': 101.6, 'low': 100.6, 'close': 101.3, 'volume': 1110}, {'open': 101.2, 'high': 101.7, 'low': 100.7, 'close': 101.4, 'volume': 1120}, {'open': 101.3, 'high': 101.8, 'low': 100.8, 'close': 101.5, 'volume': 1130}, {'open': 101.4, 'high': 101.9, 'low': 100.9, 'close': 101.60000000000001, 'volume': 1140}, {'open': 101.5, 'high': 102.0, 'low': 101.0, 'close': 101.7, 'volume': 1150}, {'open': 101.6, 'high': 102.1, 'low': 101.1, 'close': 101.8, 'volume': 1160}, {'open': 101.7, 'high': 102.2, 'low': 101.2, 'close': 101.9, 'volume': 1170}, {'open': 101.8, 'high': 102.3, 'low': 101.3, 'close': 102.0, 'volume': 1180}, {'open': 101.9, 'high': 102.4, 'low': 101.4, 'close': 102.10000000000001, 'volume': 1190}]},headers={"Authorization":"Bearer "+token("viewer")})
    assert res.status_code==403

def test_api_exposes_enterprise_control_routes():
    paths={r.path for r in app.routes}
    assert '/enterprise/health' in paths
    assert '/enterprise/v1/marketvision/features' in paths
