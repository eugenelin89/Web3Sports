# *** NOT BEING USED ***
# Original Setup file

from django.urls import path
from . import views

app_name = "mybusiness"
urlpatterns = [

    path("", views.index, name="index"),
    path("new_business", views.new_business, name="new_business"),
   
]