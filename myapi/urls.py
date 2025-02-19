# Most of the URL in myapi are accessed thru the router defined in myproject/url.py
# This file is for views that cannot be registered.
# https://stackoverflow.com/questions/70377923/attributeerror-type-object-has-no-attribute-get-extra-actions
# Cannot add generic Views in routers.
# We add the view into url here.

# *** NOT BEING USED ***
# While this is still functional, 
# *** WE ARE NO LONGER USING THIS URL ***
# File upload is now done thru FileViewSet and the URL is configured thru the router in the project urls.py

from django.urls import path
from . import views
#from django.conf.urls import url

app_name = "myapi"
urlpatterns = [
#    url(r'^upload/$', views.UploadFileView.as_view(), name='file-upload'), #r'^upload/$' is a regular expression pattern enclosed within the r prefix, indicating a raw string. 
]