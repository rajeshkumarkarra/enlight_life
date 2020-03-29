#to load admin 
from django.contrib import admin
#to give path and "include" is used for including the app.urls
from django.urls import include, path

urlpatterns =[
    path('', include('life.urls')),
    path('admin/', admin.site.urls),
]