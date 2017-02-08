from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('ScholarApiRest.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]