[![Stories in Ready](https://badge.waffle.io/pyvec/cz.pycon.org-2016.png?label=ready&title=Ready)](https://waffle.io/pyvec/cz.pycon.org-2016)
PyConCZ 2016
============

PyCon CZ is coming back to Brno for it's second edition on 28-30th October 2016.

Contributing
------------

PyCon CZ website is using Python 3.5/Django for the backend, NodeJS/webpack for
bundling frontend assets and Postgresql as a database.

### Setup dev environment

#### Using docker

Easiest way is to use [docker-compose](https://docs.docker.com/compose/):

1. Add entry to your `/etc/hosts` file. `127.0.0.1 lan.pycon.cz` on Linux. On
Mac, use `docker-machine ip` to figure out IP of your docker machine.
2. Run `docker-compose up`
3. Migrate db `docker-compose run django python manage.py migrate`

All three containers should start and you can access development version at
[http://lan.pycon.cz:8000]().

*NOTE*: If you run `docker-compose up` for the first time, it take some time
before PostgreSQL database is created. Django will try to connect to the
non-existing db which results in error message. Don't panic, just wait few
seconds :) After DB is created, you can continue and run migrations without
shutting down `docker-compose`.

#### Manually

Prepare your database: user, password and database name is `pyconcz`. Add
`127.0.0.1 db` to your `/etc/hosts`.

Inside `pyconcz_2016` directory,
run following commands to setup project for local development:

1. `mkvirtualenv -p python3.5 pyconcz`
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`

If you also want to work with styles and javascript, you need to have `node.js`.
Inside root directory (the same directory where `manage.py` is) run following commands:

1. `npm install`
2. `npm start`

Now open [http://localhost:8000]() and you should have development version of
website with webpack hot realoaing enabled.

### Building

Webpack creates static files with unique filenames (appending file hash). After
each production build, you have to commit new files. Don't care about the old
ones at the moment.

1. `npm run build` (or `docker-compose run webpack npm run build` when using docker)
2. `git add pyconcz_2016/static_build`


License
-------

This work is licensed under a [MIT](./LICENSE.md)
