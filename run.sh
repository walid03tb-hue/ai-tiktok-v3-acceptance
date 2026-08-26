#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$ROOT/verify_integrity.py"
python3 "$ROOT/tests/test_case_catalog.py"
echo "EXTERNAL_ACCEPTANCE_HARNESS_PASS: integrity + protected case catalog"
