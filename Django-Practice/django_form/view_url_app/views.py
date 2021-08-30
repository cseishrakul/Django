from django.shortcuts import render
from django.http import HttpResponse
from view_url_app.models import Musician, Album
from view_url_app import forms
# Create your views here.


def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1': 'list of Musician', 'musician': musician_list}
    return render(request, 'view_url_app/index.html', context=diction)


def form(request):
    new_form = forms.MusicianForm()
    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    diction = {'test_form': new_form, 'heading': 'Add New'}

    return render(request, 'view_url_app/form.html', context=diction)




















# exercise
# new_form = forms.user_form()
# diction = {'test_form': new_form, 'heading': "This is created by django form"}
#
# if request.method == 'POST':
#     new_form = forms.user_form(request.POST)
#     diction.update({'test_form':new_form})
#     if new_form.is_valid():
#         # user_name = new_form.cleaned_data['user_name']
#         # user_dob = new_form.cleaned_data['user_dob']
#         # user_email = new_form.cleaned_data['user_email']
#         # boolean_field = new_form.cleaned_data['boolean_field']
#         # char_field = new_form.cleaned_data['char_field']
#         # field = new_form.cleaned_data['field']
#         # name = new_form.cleaned_data['name']
#         # number = new_form.cleaned_data['number']
#
#         # diction.update({'user_name': user_name})
#         # diction.update({'user_email': user_email})
#         # diction.update({'user_dob': user_dob})
#         # diction.update({'boolean_field': boolean_field})
#         # diction.update({'char_field': char_field})
#         # diction.update({'field': field})
#         # diction.update({'name': name})
#         # diction.update({'number': number})
#         diction.update({'field': 'Matches'})
#         diction.update({'form_submitted': 'Done'})
