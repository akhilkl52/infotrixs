
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
urlpatterns = [

        path("",views.home),
        path('search/',views.searchID,name='search'),

        ]