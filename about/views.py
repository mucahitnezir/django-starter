from django.utils.translation import ugettext as _
from django.views.generic import ListView

from .models import TeamMember
from setting.models import Setting


class AboutView(ListView):
    model = TeamMember
    template_name = 'about/index.html'

    def get_queryset(self):
        return TeamMember.objects.all()

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['about_us'] = Setting.get_one('about_page_content')
        data['title'] = _('About')
        return data
