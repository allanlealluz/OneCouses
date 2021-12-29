from django.urls import path
from . import views
app_name = 'oneapp'
urlpatterns = [
path('',views.index,name='index')
    ]