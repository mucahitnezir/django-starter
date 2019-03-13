FROM python:3.6

WORKDIR /app

# Update package versions
RUN apt-get update

# Install Nodejs
RUN apt-get install sudo
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN sudo apt-get install -y nodejs
RUN node -v && npm -v

# Insall gettext for i18n
RUN apt-get install -y gettext libgettextpo-dev

# Firstly, copy requirements file
COPY requirements.txt /app/requirements.txt

# Install requirement packages
RUN pip install -r requirements.txt

# Copy all project folders
COPY . /app

# Install npm packages
RUN npm install

# Compile .po files
RUN python manage.py compilemessages -l tr
RUN python manage.py compilemessages -l en

EXPOSE 8000
