#!/bin/bash
set -e

echo "Começando o build..."

python3 -m venv venv
source venv/bin/activate
pip install pytest
