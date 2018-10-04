# Awesome Face Emotion Detection

This repo contain the code of Machine Learning Services for Awesome - a platform of education management.

# Install Dependencies

```
pip install -r requirements.txt
```

# Config .env file

```
cp .env-example .env
```
Config `.env` with your enviroiment variables 

## Config database 

```
'DB_ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
'DB_NAME': 'sqlite3.db',                      # Or path to database file if using sqlite3.
'DB_USER': '',                      # Not used with sqlite3.
'DB_PASSWORD': '',                  # Not used with sqlite3.
'DB_HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
'DB_PORT': '',                      # Set to empty string for default. Not used with sqlite3.

```

# Make migrations

```
python manage.py makemigrations
python manage.py migrate
```
# Main features

##  Auto detect emotion from video
* Auto find the emotion of frames from video
* Require: 
    * Video with *.mp4* format

   