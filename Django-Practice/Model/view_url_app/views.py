from django.shortcuts import render
from django.http import HttpResponse
from view_url_app.models import Musician, Album
# Create your views here.


def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1': 'list of Musician', 'musician': musician_list}
    return render(request, 'view_url_app/index.html', context=diction)
