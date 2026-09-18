# Deployment checklist — SYNERGY MarketVision

- [ ] Pin revision/image and rerun tests.
- [ ] Customer TLS + OIDC/mTLS/JWKS and KMS secrets.
- [ ] Define market-data confidentiality/retention policy.
- [ ] Validate OHLCV schema, missing data and window bounds.
- [ ] Exercise `/enterprise/v1/marketvision/features` at representative bar/window sizes.
- [ ] Trace request ID to audit.
- [ ] Benchmark memory/latency and downstream OOS model value.
- [ ] Keep any trading execution outside this feature service.