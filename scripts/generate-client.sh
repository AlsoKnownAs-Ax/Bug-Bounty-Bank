#!/usr/bin/env bash

# Exit on error, print commands
set -e
set -x

# Change to project root directory
cd "$(dirname "$0")/.."

# Generate OpenAPI spec
PYTHONPATH=server python -c "from src.main import app; import json; print(json.dumps(app.openapi()))" > openapi.json

# Move spec to frontend directory
mv openapi.json client/

# Generate client
cd client 
npm run generate-client