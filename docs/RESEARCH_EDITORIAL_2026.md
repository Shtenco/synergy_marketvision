# MARKETVISION — scientific research and engineering study

> MarketVision converts price and volume observations into a structured perception layer. Its contribution is not a promised trading signal, but a deterministic, contract-bound representation that can be consumed by independent quantitative systems.

## Research hypothesis

$$r_t=\log(\max(C_t,\varepsilon))-\log(\max(C_{t-1},\varepsilon)),\qquad z_{t,j}=\frac{x_{t,j}-\operatorname{median}(x_{\cdot,j})}{\operatorname{IQR}(x_{\cdot,j})}.$$

### Implemented scientific mechanism

The actual \`market_cube(frame, window=64)\` requires OHLCV columns, takes the last T bars and constructs four channels of economic features: log closing returns, relative high–low range, logarithmic volume and return sign. Median/IQR robust scaling is applied feature-by-feature, with zero IQR replaced by 1. The output stacks **signed scaled values, absolute values and signs**, yielding a float32 tensor of shape **(3, T, 4)**.

The source clips nonpositive closes to 1e-12 for log transforms, clips negative volume to zero and computes the first return of a window as zero. These are explicitly defined boundary conventions that permit deterministic replay. The \`summary_features\` function exposes mean, standard deviation and mean squared energy for model diagnostics. They describe a representation, not expected return.

### Architecture and distinct value

| Layer | Real source | Contribution |
|---|---|---|
| Tensor construction | [core.py](../src/synergy_marketvision/core.py) | Source-normalized, shape-stable feature cube |
| Typed payload | [synergy_contracts.py](../src/synergy_marketvision/synergy_contracts.py) | \`observation_id\`, symbol, window and advisory-only output |
| Market ingestion | [enterprise/adapters](../src/synergy_marketvision/enterprise/adapters/) | MT5, CCXT and Bybit integration surfaces |
| Service layer | [enterprise/service.py](../src/synergy_marketvision/enterprise/service.py) | API orchestration, logging and business boundaries |
| Tests | [tests](../tests/) | Core, contracts, enterprise and adapters |

**Interesting research question:** does the signed/absolute/sign tensor improve unseen-regime detection compared with raw OHLCV and z-score features when all consumers use precisely the same data availability timestamps?

### Falsifiable programme

Use at least three volatility regimes, a fixed train/validation/test calendar and symbol-held-out tests. Check shape/finite invariants, outliers, duplicate timestamps, zero volumes, weekend gaps, scaling drift and NaN handling. Compare robust scaling on the *entire observed window* to a causal rolling fit; neither has permission to use bars from the future relative to prediction time. Report model downstream uplift, not invented standalone MarketVision PnL.

### Quick reproduction

\`\`\`bash
python -m pip install -e '.[dev]'
python -m pytest -q tests/test_core.py tests/test_synergy_contracts.py
\`\`\`

The actual dependency extras should be checked against the repository's package metadata before installing. This documentation update does not claim execution of the test suite.

## Evidence model

Research claims are tied to source paths, frozen datasets and exactly identified evaluation protocols. Architecture and code establish mechanisms; measured tests establish behaviour under stated conditions. Production deployment and financial efficacy are distinct evidence classes.

## Contribution to SYNERGY

The module owns its domain-specific scientific function without acquiring trading, payment or financial accounting authority merely because another service consumes its output.
