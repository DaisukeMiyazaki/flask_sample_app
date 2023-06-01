#!/bin/bash
chmod +x ./migration/initialize_migration.sh
FLASK_APP=main.py flask db init