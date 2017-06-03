from django.conf.urls import url
from . import views

urlpatterns = [
    # for login page
    url(r'^login$', views.index, name='index'),
    
    # this is not a webpage but it is used for checking gmail authentication
    url(r'^gverify$', views.gverify, name='gverify'),
    
    # this page shows the eigible scholarships for a student
    url(r'^eligible$', views.eligible, name='eligible'),
]
