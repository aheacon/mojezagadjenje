#!/usr/bin/env bash
cd /home/anel/aheacon/mojezagadjenje
source env/bin/activate
cd my_pollution/
python manage.py cron_job


