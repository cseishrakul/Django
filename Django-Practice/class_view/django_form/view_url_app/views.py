from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from view_url_app import models
from django.urls import reverse_lazy


class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'view_url_app/index.html'


class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'view_url_app/musician_detail.html'


class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'view_url_app/musician_form.html'


class UpdateMusician(UpdateView):
    fields = ('first_name', 'instrument')
    model = models.Musician
    template_name = 'view_url_app/musician_form.html'


class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('view_url_app:index')
    template_name = 'view_url_app/delete_musician.html'


# class IndexView (TemplateView):
#     template_name = 'view_url_app/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['sample_data_1'] = "Sample Data 1"
#         context['sample_data_2'] = "Sample Data 2"
#         return context

# class IndexView(View):
#     def get(self, request):
#         return HttpResponse('Hello Class')
