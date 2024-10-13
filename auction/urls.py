from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="home"), 
    path("items/<category>", views.items, name="items"), 
    path("login", views.login_page, name="login"),
    path("", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("post-Item", views.post_item, name="postitem"),
    path("MyItems", views.user_items, name="useritems"),
    path("about", views.about_page, name="about"),
]
