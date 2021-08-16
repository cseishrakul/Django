from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#
def index(request):
    diction={'text_1':'I am learning django'}
    return render(request,'view_url_app/index.html',context=diction)
