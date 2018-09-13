# Django Blog
Hello, this is basic django web application template to build new web sites. This application is powered by @mucahitnezir.

## Demo
Demo application is hosted in PythonAnywhere. You can reach it from [this link](https://mucahitnezir.pythonanywhere.com).

## Required Environments
1. Env Name: `EVNIRONMENT`. Available values: `development` or `production`
2. Env Name: `SENDGRID_API_KEY`. You have to define this environment if you send the email from contact form.

## Installation
Perform the following steps after downloading the project.

1. Install virtualenv (If it is not installed)  
`pip install virtualenv`
2. Create new virtualenv in project root direction.  
`virtualenv venv`
3. Activate your virtualenv  
**Linux & Mac:** `source venv/bin/activate`  
**Windows:** `venv\Scripts\activate`
4. Install required packages  
`pip install -r requirements.txt`
5. Create migration files  
`python manage.py makemigrations`
6. Migrate db from migration files  
`python manage.py migrate`
7. Create super user  
`python manage.py createsuperuser`
8. Collect static files (Only required in production)  
`python manage.py collectstatic`
9. Run server  
`python manage.py runserver`
