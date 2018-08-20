from django.shortcuts import render


def home_view(request):
    context = {
        'title': 'Anasayfa'
    }
    return render(request, 'homepage.html', context)
