
# Angular 6 and Django REST Framework

A simple example application where an Angular 6 app talks to an API running
Django REST framework.

# Setup

Install dependencies and run migrations to set up the app:

## Create Virtual Environment
```
virtualenv env
source virtualenv/bin/activate
```

## Install dependencies and setup data

```
pip install -r requirements.txt
cd server
python manage.py migrate
```

## Install Angular 6 dependencies

```
cd ../client
npm install
```

## Run the app

Run the REST server:

```
# in the server folder
python manage.py runserver
```

Start the Angular 6 app:

```
# in the client folder
npm start
```

