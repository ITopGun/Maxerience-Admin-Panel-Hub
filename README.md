# A love for food

version @1.0.0

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
	pip3 install -r requirements.txt
	python manage.py collectstatic
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py runserver
```

## Database Settings

This app used SQLite for the database, so database settings are not required.

## Static Files

Static files are in /static/ directory.

## Templates Files

Templates files are in /template/ directory.

## Python Files

Python files are in /front/ directory.

## Uploaded images

Uploaded images are stored in /media/images/ directory.

## Structure of Project

```bash
< PROJECT ROOT >        # sqlite file
	│   manage.py
	│   README.md
	│   requirements.txt        # python libraries for this app.
	│
	├───front
	│   │   admin.py
	│   │   apps.py
	│   │   models.py            # define Recipe table
	│   │   tests.py
	│   │   urls.py              # define URLs and combine URLs and view files
	│   │   __init__.py
	│   │
	│   ├───migrations
	│   │
	│   ├───views
	│   │   │
	│   │   ├───auth
	│   │   │   │   login.py      # user login
	│   │   │   │   signup.py     # user sign up
	│
	├───media
	│   └───images
	│
	├───maxerience
	│   │   asgi.py
	│   │   settings.py                    # main setting file of this app.
	│   │   urls.py
	│   │   wsgi.py
	│
	├───static               # plugin to input multiple words
	│
	└───templates
```

## Demo
[DEMO](http://143.198.187.223/)