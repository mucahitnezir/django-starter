import os


# Get environment
environment = os.environ.setdefault('ENVIRONMENT', 'development')

# Load settings file
if environment == 'development':
    from.setting.development import *
elif environment == 'production':
    from .setting.production import *
else:
    from .setting.development import *
