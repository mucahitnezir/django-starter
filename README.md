# Django Starter
Hello, this is basic django web application. This application is powered by @mucahitnezir.

## 1. Demo
Demo application is hosted in AWS ElasticBeanstalk. You can reach it from [this link](http://django-starter.mucahitnezir.com).

## 2. Database Selection
This project uses **PostgreSQL** database.

## 3. Installation
Perform the following steps after downloading the project.

### 3.1. Installation with Docker Compose
1. Create and modify `.env` file by copying `.env.sample` file in root directory.
2. After, you have to build docker containers with `docker-compose build` command.
3. Run `docker-compose run web python manage.py migrate` command to migrate database.
3. Run `docker-compose run web python manage.py loaddata setting/fixtures/parameter.json` command to load initial database rows.
4. Run `docker-compose run web python manage.py createsuperuser` command to create admin user.
5. Run `docker-compose up` command to run server.

### 3.2. Manuel Installation

1. Install virtualenv (If it is not installed)  
`pip install virtualenv`
2. Create new virtualenv in project root direction.  
`virtualenv venv`
3. Activate your virtualenv  
**Linux & Mac:** `source venv/bin/activate`  
**Windows:** `venv\Scripts\activate`
4. Install required packages  
`pip install -r requirements.txt`
5. Create and modify `.env` file by copying `.env.sample` file in root directory.
6. Migrate db from migration files  
`python manage.py migrate`
7. Load initial database rows  
`python manage.py loaddata setting/fixtures/parameter.json`
8. Create super user  
`python manage.py createsuperuser`
9. Install npm packages.  
`npm install`
10. Collect static files (Only required in production)  
`python manage.py collectstatic`
11. Compile language files.  
`python manage.py compilemessages -l tr`  
`python manage.py compilemessages -l en`
12. Run server  
`python manage.py runserver`
