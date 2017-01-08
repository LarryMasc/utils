# Prepare a virtualenv 
  * sudo easy_install pip
  * pip install virtualenv
  * Review /usr/local/bin/virtualenvwrapper.sh script to setup.
  * Set VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 in .bashrc before
    sourcing the virtualenvwrapper.sh
  * sudo apt install python-django (or python3-django)
  * cd /u/gitwork/utils/django
  * django-admin startproject bookstore
  * ./manage.py migrate (migrates a SQLite3 DB. look in settings.py)
  * ./manage.py runserver

  * Add to GIT