from django.conf.urls import url
from django.urls import path, include
from .views import (
    SiteListApiView,
)

urlpatterns = [
    path('api', SiteListApiView.as_view()),
]