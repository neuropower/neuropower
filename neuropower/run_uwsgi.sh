#!/bin/bash
source /usr/share/fsl/5.0/etc/fslconf/fsl.sh
PATH=/usr/lib/python2.7:$PATH
export PATH
which python
python manage.py makemigrations --merge --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
uwsgi uwsgi.ini
