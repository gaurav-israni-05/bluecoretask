# README #

This README would normally document whatever steps are necessary to get your application up and running.

### Dependencies ###

* Python 3.x
* PostGreSQL 9.x


### Getting Started ###

* Create a user for postgres : "CREATE USER bluecore_user WITH PASSWORD XXX ;"
* Create a database for the application : "CREATE DATABASE bluecore_email;"
* Grant all priveleges on database to user : "GRANT ALL PRIVILEGES ON DATABASE bluecore_email to bluecore_user;"


### Virtual Environment Setup ###

* Setup tribe virtualenv : "virtualenv -p python3 bluecore"
* Move to virtualenv and activate its environment


### Dependency Setup ###

* Install requirements: "pip install -r requirements.txt".
* In settings.py, change <DB_PASSWORD>
* Run migrations: "python manage.py migrate"

### Run a celery worker ###
* Open another terminal and cd into bluecore_email_systems folder 
* Run the following command in termial: celery -A bluecore_email_systems  worker -l info

