# Benchmarks and acceptance — SYNERGY MarketVision

**19 tests passed**. Local health smoke: **80/80 HTTP 200**, p50 **13.7 ms**, p95 **62.4 ms**, p99 **70.3 ms**, ~**630 req/s**.

Health smoke only. Customer acceptance must separately benchmark `/enterprise/v1/marketvision/features` across representative bar counts/windows, memory usage and downstream OOS incremental value versus simpler features.