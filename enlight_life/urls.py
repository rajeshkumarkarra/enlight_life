#to load admin 
from django.contrib import admin
#to give path and "include" is used for including the app.urls
from django.urls import include, path

urlpatterns =[
    path('life', include('life.urls')),
    path('', include('ngo.urls')),
    path('hi', include('hi.urls')),
    path('admin/', admin.site.urls),
]