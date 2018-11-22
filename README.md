# Django Blog
Hello, this is basic django web application template to build new web sites. This application is powered by @mucahitnezir.

## Demo
Demo application is hosted in PythonAnywhere. You can reach it from [this link](https://mucahitnezir.pythonanywhere.com).

## Database Selection
This project uses **PostgreSQL** database.

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
5. Create `.env` file by copying `.env.sample` file in root directory.
6. Modify **.env** file.
7. Create migration files  
`python manage.py makemigrations`
8. Migrate db from migration files  
`python manage.py migrate`
9. Create super user  
`python manage.py createsuperuser`
10. Install npm packages.  
`npm install`
11. Collect static files (Only required in production)  
`python manage.py collectstatic`
12. Compile language files.  
`python manage.py compilemessages -l tr`  
`python manage.py compilemessages -l en`
13. Run server  
`python manage.py runserver`
