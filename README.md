# SYNERGY MarketVision

> **3D/CV-ready market-state tensors and alternative feature generation for quant research**

**Enterprise v2.0.0** · FastAPI/OpenAPI · Docker/Compose · RBAC/JWT · PostgreSQL/ClickHouse audit

**Designed for:** Quant research teams, systematic funds, prop firms and alternative-data teams  
**Primary endpoint:** `POST /enterprise/v1/marketvision/features`

> [!IMPORTANT]
> Feature-generation infrastructure only. Alternative representations do not guarantee predictive power or trading profit.

## Verification
**19 tests passed** · health smoke **80/80 200** · local p95 **62.4 ms** (~630 req/s). Health smoke only.

## Quick start
```bash
pip install -e '.[dev,enterprise]'
pytest -q
python -m synergy_marketvision.api
```

## CTO package
[Due diligence](docs/CTO_DUE_DILIGENCE.md) · [Architecture](docs/ARCHITECTURE_DIAGRAMS.md) · [API](docs/API_EXAMPLES.md) · [Security](SECURITY.md) · [Benchmarks](docs/BENCHMARKS_AND_ACCEPTANCE.md) · [SLA/SLO](docs/SLA_SLO.md) · [Deployment](docs/DEPLOYMENT_CHECKLIST.md) · [Pilot](docs/CUSTOMER_PILOT.md)
