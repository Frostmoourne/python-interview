from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Items


class ItemsListView(ListView):
    model = Items
    template_name = 'mainapp/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        items = Items.objects.all()
        return items


class ItemsAddView(CreateView):
    model = Items
    template_name = 'mainapp/add_item.html'
    success_url = reverse_lazy('mainapp:index')
    fields = '__all__'
