from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("foo", views.foo, name="foo"),
    path("bar", views.bar, name="bar"),
    path("foobar", views.foobar, name="foobar")
]