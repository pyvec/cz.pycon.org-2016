[![Stories in Ready](https://badge.waffle.io/pyvec/cz.pycon.org-2016.png?label=ready&title=Ready)](https://waffle.io/pyvec/cz.pycon.org-2016)
PyConCZ 2016
============

PyCon CZ is coming back to Brno for it's second edition on 28-30th October 2016.

Contributing
------------

PyCon CZ website is using Django and Python 3.5. Inside `pyconcz_2016` directory, 
run following commands to setup project for local development:

1. `mkvirtualenv -p python3.5 pyconcz`
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`

If you also want to work with styles and javascript, you need to have `node.js`. Inside `pyconcz_2016/pyconcz_2016` directory (the same directory where `manage.py` is) run following commands:

1. `npm install`
2. `npm start`

Now open `http://localhost:8000` and you should have development version of website with webpack hot realoading enabled.

License
-------

This work is licensed under a [MIT](./LICENSE.md)
