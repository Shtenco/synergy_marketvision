# API examples — SYNERGY MarketVision

`POST /enterprise/v1/marketvision/features` — roles **researcher, trader**.

```json
{"window":4,"bars":[{"open":100,"high":101,"low":99,"close":100.2,"volume":1000},{"open":100.2,"high":101.2,"low":99.8,"close":100.5,"volume":1100},{"open":100.5,"high":101.5,"low":100,"close":101,"volume":1200},{"open":101,"high":102,"low":100.5,"close":101.4,"volume":1300}]}
```

Expected response includes `shape`, `energy`, feature summary fields and `request_id`. Canonical schema: `/docs`.