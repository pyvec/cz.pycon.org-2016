PyConCZ 2016
============

PyCon CZ is coming back to Brno for it's second edition on 28-30th October 2016.

Contributing
------------

PyCon CZ website is using Python 3.5/Django for the backend, NodeJS/webpack for
bundling frontend assets and Postgresql as a database.

### Setup dev environment

#### Manually

Inside `pyconcz_2016` directory,
run following commands to setup project for local development:

1.  Prepare postgresql database: user `pyconcz`, password empty, database `pyconcz`

    E.g. on Mac:

    ```
    $ createuser --pwprompt pyconcz
    $ createdb -Opyconcz -Eutf8 pyconcz
    ```

2.  `python3 -m venv env`
3.  `pip install -r requirements-dev.txt`
4.  `./manage.py migrate`
5.  `./manage.py runserver`
6.  Open [http://localhost:8000]()

If and **only if** you also want to work with styles and javascript, you need to have `node.js`.
Inside root directory (the same directory where `manage.py` is) run following commands:

1.  Add following line to your `/etc/hosts` file: `127.0.0.1 lan.pycon.cz`.
2.  `npm install`
3.  `npm start`

Now open [http://lan.pycon.cz:8000]() and you should have development version of
website with webpack hot reloading enabled.

### Building

**You only need this when you changed styles**. Webpack creates static files with unique filenames (appending file hash). After
each production build, you have to commit new files. Don't care about the old
ones at the moment.

1. `npm run build` (or `docker-compose run webpack npm run build` when using docker)
2. `git add pyconcz_2016/static_build`


License
-------

This work is licensed under a [MIT](./LICENSE.md)
