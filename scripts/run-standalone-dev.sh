#! /usr/bin/env bash
# This script must not be used for production. Migration scripts
#  should be done by different jobs in a different layer.

set -e

bash scripts/tcp-port-wait.sh $DATABASE_HOST $DATABASE_PORT

# Run migrations
alembic upgrade head

# Start Gunicorn
gunicorn -k "uvicorn.workers.UvicornWorker" -c "/code/gunicorn_conf.py" "app.main:app" --reload
