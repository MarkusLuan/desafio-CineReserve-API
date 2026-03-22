#!/bin/bash
echo "Esperando pelo banco..."
sleep 20
# Segura por uns 20 segundos...
# Nenhum outro script para esperar o banco funcionou e tou morto de sono

poetry run migrate --config docker
poetry run seed --config docker
exec "$@"