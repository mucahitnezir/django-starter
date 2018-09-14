from django.shortcuts import render
from django.utils.translation import ugettext as _


def home_view(request):
    context = {
        'title': _('Homepage')
    }
    return render(request, 'homepage.html', context)
