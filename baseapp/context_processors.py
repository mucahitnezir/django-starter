import os

from setting.models import Setting


def parameters(request):
    # Get parameters
    params = Setting.get_multiple(['gtm_container_id', 'company_name'])
    params['environment'] = os.environ.get('ENVIRONMENT')
    # Return all
    return {
        'parameters': params
    }
