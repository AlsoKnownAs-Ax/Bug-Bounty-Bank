:: Make sure you are in the client directory for this to work

@echo off
setlocal EnableExtensions EnableDelayedExpansion

:: Change to project root directory
cd %~dp0\..

:: Generate OpenAPI spec
set PYTHONPATH=server
python -c "from src.main import app; import json; print(json.dumps(app.openapi()))" > openapi.json 

:: Move spec to client directory
move openapi.json client\

:: Generate client
cd client 
npm run generate-client

