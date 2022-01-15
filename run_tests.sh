#!/bin/bash

pytest --cov-report=term-missing --cov=cars/ --disable-network -x --cov-fail-under=90 || exit 1