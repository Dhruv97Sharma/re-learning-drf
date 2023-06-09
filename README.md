# Relearning DRF

This is a simple DRF project for learning django rest framework capabilities from the official documentation tutorial [here](https://www.django-rest-framework.org/tutorial/quickstart/).

## Features

- Django 3.0+
- Uses [venv](https://docs.python.org/3/library/venv.html) - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.
- Using Neon Tech PostgreSQL managed DB [neon.tech](https://neon.tech/docs/introduction).


## How to install

```bash
$ source .env
$ python -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

## Environment variables

Since I am using neon tech postgres managed DB for this example, this is how you would need to setup the database url variable in a .env file. The `DATABASE_URL` variable loads the correct settings, you can add the url to your DB here

```
export DATABASE_URL=postgres://<your_username>:<your_password>@<db_branch_id>.us-east-2.aws.neon.tech/drf_tutorial_db?options=endpoint%3D<db_branch_id>
```

With this you can setup your neon tech db with the name 'drf_tutorial_db' and add your db url here.

## Deployment

It is possible to deploy to Heroku or to your own server.


## License

The MIT License (MIT)
