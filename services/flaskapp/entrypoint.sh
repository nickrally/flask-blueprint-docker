#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Script executed from: ${PWD}"
ls -l
export PYTHONPATH=.
python project/manage.py create_db 

exec "$@"