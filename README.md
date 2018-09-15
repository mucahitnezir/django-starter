# Django Blog
Hello, this is basic django web application template to build new web sites. This application is powered by @mucahitnezir.

## Demo
Demo application is hosted in PythonAnywhere. You can reach it from [this link](https://mucahitnezir.pythonanywhere.com).

## Database Selection
This project uses **sqlite3** in the development environment, and **PostgreSQL** in the production environment.

## Required Environments
1. Env Name: `EVNIRONMENT`. Available values: `development` or `production`
2. Env Name: `SENDGRID_API_KEY`. You have to define this environment if you want to send email from contact form.
3. Environment for SECRET_KEY (in settings.py): `SECRET_KEY`.
4. Recaptcha Environments: `RECAPTCHA_PUBLIC_KEY` and `RECAPTCHA_PRIVATE_KEY`.
5. Database Environments (only required in production environment. DB driver is postgresql): `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` and `DB_PORT`

## Installation
Perform the following steps after downloading the project.

1. Install virtualenv (If it is not installed)  
`pip install virtualenv`
2. Create new virtualenv in project root direction.  
`virtualenv venv`
3. Activate your virtualenv  
**Linux & Mac:** `source venv/bin/activate`  
**Windows:** `venv\Scripts\activate`
4. Define required environment variables.
5. Install required packages  
`pip install -r requirements.txt`
6. Create migration files  
`python manage.py makemigrations`
7. Migrate db from migration files  
`python manage.py migrate`
8. Create super user  
`python manage.py createsuperuser`
9. Install bower packages. (bower npm package has to be installed globally via `npm install -g bower`)  
`bower install`
10. Collect static files (Only required in production)  
`python manage.py collectstatic`
11. Compile language files.  
`python manage.py compilemessages -l tr`  
`python manage.py compilemessages -l en`
12. Run server  
`python manage.py runserver`
