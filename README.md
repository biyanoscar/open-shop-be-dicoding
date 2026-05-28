# open-shop-be-dicoding

## Setup

Install dependencies:
```
pipenv install
```

Activate virtual environment:
```
pipenv shell
```

## Running the Application

Create the DB tables first:
```
python manage.py migrate
```

Run the development web server:
```
python manage.py runserver
```

Open the URL http://localhost:8000/ to access the application.
