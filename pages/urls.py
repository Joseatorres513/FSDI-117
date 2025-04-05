from django.urls import path
from .views import HomePageView, AboutPageView, contact_form_view, testing_view
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", contact_form_view, name="contact_form"),
    path("testing_page/", testing_view, name="testing_page"),
    path("contact2/", views.contact_view, name="contact"),
]
