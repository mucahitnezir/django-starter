from django.shortcuts import render

from .models import TeamMember
from setting.models import Setting


def about_index(request):
    # Page context
    context = {
        'title': 'About',
        'about_us': Setting.get_one('about_page_content'),
        'team_members': TeamMember.objects.all()
    }
    # Render page
    return render(request, 'about/index.html', context)
