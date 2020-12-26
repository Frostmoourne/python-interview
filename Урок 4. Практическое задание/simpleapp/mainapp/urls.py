from django.urls import path

from .views import ItemsListView, ItemsAddView

app_name = 'mainapp'

urlpatterns = [
    path('', ItemsListView.as_view(), name='index'),
    path('add_item/', ItemsAddView.as_view(), name='add')
]