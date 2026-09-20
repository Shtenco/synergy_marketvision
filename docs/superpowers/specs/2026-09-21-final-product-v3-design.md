# MarketVision V3 Final Product Design

**Version:** 3.0.0  
**Branch:** `production/v3.0.0`  
**Status:** architecture specification for human review

## Goal
Convert MarketVision from a one-shot OHLCV cube summary endpoint into a feature-engineering platform with versioned feature definitions, feature jobs, immutable artifacts, data lineage and reproducible checksums.

## Current gap
Today bars are posted directly and only summary statistics are returned. No FeatureSetVersion, dataset identity, artifact checksum or persistent job exists.

## Durable resources
- DatasetReference
- FeatureSetDefinition
- FeatureSetVersion
- TransformationGraph
- FeatureJob
- FeatureArtifact

## Core invariants
1. Feature definitions are immutable by version.
2. Every artifact references dataset hash + feature-set version + code version.
3. Same dataset+feature definition may be idempotently reused.
4. Artifact metadata is authoritative in PostgreSQL.
5. Large arrays may live in object storage; checksum/URI remain authoritative metadata.
6. Feature generation success is not equivalent to predictive/OOS validation.
7. Input data-quality failures are explicit artifacts/errors, never silently coerced.

## V3 API
- `POST /enterprise/v3/datasets`
- `POST /enterprise/v3/feature-sets`
- `GET /enterprise/v3/feature-sets/{id}`
- `POST /enterprise/v3/feature-jobs`
- `GET /enterprise/v3/feature-jobs/{id}`
- `GET /enterprise/v3/feature-artifacts/{id}`

## Persistence
PostgreSQL:
- dataset_references
- feature_set_definitions
- feature_set_versions
- transformation_graphs
- feature_jobs
- feature_artifacts
- idempotency_keys
- audit_events

## Artifact metadata
Includes shape, dtype, checksum, artifact URI or inline payload marker, dataset SHA-256, feature-set version, transformation graph hash, code version, created_at and request_id.

## Data-quality rules
Reject non-finite OHLC, invalid high/low relationships, negative volume if policy forbids it, insufficient rows, impossible window, invalid timestamps and malformed ordering.

## Acceptance gates
- artifact reproducible from same dataset/version;
- checksum stable;
- process restart preserves job/artifact metadata;
- object-store failure is explicit if configured;
- tenant isolation;
- DB outage -> readiness 503;
- idempotent job creation;
- V2 tests remain green.
