# Architecture — SYNERGY MarketVision

```mermaid
flowchart LR
A[OHLCV bars]-->B[RBAC API]
B-->C[MarketVision Core]
C-->D[3D/CV-ready tensor]
D-->E[Feature summary]
E-->F[Audit + request ID]
F-->G[(PostgreSQL)]
F-->H[(ClickHouse)]
E-->I[Downstream customer model]
```

Primary endpoint: `/enterprise/v1/marketvision/features`. Generated representations/features do not imply predictive power; downstream OOS validation is required.