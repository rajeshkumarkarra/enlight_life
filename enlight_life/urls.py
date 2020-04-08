#to load admin 
from django.contrib import admin
#to give path and "include" is used for including the app.urls
from django.urls import include, path
# for media files
from django.conf import settings
# for media files
from django.conf.urls.static import static

urlpatterns =[
    path('life', include('life.urls')),
    path('', include('ngo.urls')),
    path('hi', include('hi.urls')),
    path('admin/', admin.site.urls),
]
# for media files
urlpatterns = urlpatterns +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)