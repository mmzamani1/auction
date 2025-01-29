from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("auction/", include("auction.urls")),
    path("weather/", include("weatherApp.urls")),
    path('admin/', admin.site.urls),
]
