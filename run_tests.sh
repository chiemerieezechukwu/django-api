#!/bin/bash
set -xe

pytest --cov-report=term-missing --cov=cars --disable-network -x --cov-fail-under=90 || exit 1

echo "writing coverage..."

coverage json