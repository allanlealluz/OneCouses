from django.urls import path
from . import views
app_name = 'oneapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.logins,name='logins')
    ]