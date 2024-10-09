from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("login", views.login_page, name="login"),
    path("", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("post-Item", views.post_item, name="postitem"),
    path("about", views.about_page, name="about"),
]
