from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Avtomobile
from .forms import Avto
from django.views import View
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView

class AvtoListView(ListView):
    model = Avtomobile
    template_name = 'avtos.html'
    context_object_name = 'avtos'


    def get_context_data(self, **kwargs):
        context = super(AvtoListView, self).get_context_data(**kwargs)
        avtos = Avtomobile.objects.all()
        context['avtos'] = avtos
        return context

class AvtoDetailView(DetailView):
    model = Avtomobile
    template_name = 'avto.html'
    context_object_name = 'avto'

class AvtoDeleteView(DeleteView):
    model = Avtomobile
    template_name = 'delete.html'
    success_url = reverse_lazy('avtos')

class AvtoCreateView(CreateView):
    model = Avtomobile
    template_name = 'avto-create.html'
    fields = ('model', 'year', 'color', 'price', 'image')
    success_url = reverse_lazy('avtos')

class AvtoUpdateView(UpdateView):

    model = Avtomobile
    template_name = 'avto-update.html'
    context_object_name = 'avto'
    fields = ('model', 'year', 'color', 'price', 'image')

    def get_success_url(self):
        return reverse_lazy('avto', kwargs={'pk': self.object.id})