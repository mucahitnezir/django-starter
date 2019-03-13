FROM python:3.6

WORKDIR /app

COPY requirements.txt /app/requirements.txt

# Install requirement packages
RUN pip install -r requirements.txt

# Insall gettext for i18n
RUN apt-get update -y && apt-get install -y gettext libgettextpo-dev

COPY . /app

# Compile .po files
RUN python manage.py compilemessages -l tr
RUN python manage.py compilemessages -l en

EXPOSE 8000
