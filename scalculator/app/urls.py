from django.conf.urls import url
from . import views

urlpatterns = [
    # for login page
    url(r'^login$', views.login, name='login'),

    # this is not a webpage but it is used for checking gmail authentication
    url(r'^gverify$', views.gverify, name='gverify'),

    # this page shows the eigible scholarships for a student
    url(r'^eligible$', views.eligible, name='eligible'),

    # this page shows saved scholarships by the user
    url(r'^saved$', views.saved, name='saved'),

    # this page is for webmail verification for iitg students
    url(r'^wverify$', views.wverify, name='wverify'),

    # this page has information about the user
    url(r'^profile$', views.profile, name='profile'),

    # this page is for first time experience for filling profile data
    url(r'^fxprofile$', views.fxprofile, name='fxprofile'),

    # this page is for first time experience for webmail verification
    url(r'^fxwver$', views.fxwver, name='fxwver'),

    # this function is for logout
    url(r'^glogout$', views.glogout, name='glogout'),

    # this function is for marking scholarship
    url(r'^mark$', views.mark, name='mark'),
]
