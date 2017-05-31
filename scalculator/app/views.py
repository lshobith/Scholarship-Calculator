from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


'''
this page has two types of login:
1. login with webmail.
2. login with gmail.
'''
def index(request):
    return HttpResponse("login page.")

'''
an IITG student who has logged in using gmail
can view scholarships of IITG after verifying
with webmail ID and password in this page.

this verification is needed only once.
'''
def verification(request):
    return HttpResponse("iitg verification.")

'''
students enter their details in this page.
'''
def student_details(request):
    return HttpResponse("enter your details.")

'''
all scholarships a student is eligible to
apply are shown in this page.
'''
def eligible_scholarships(request):
    return HttpResponse("scholarships you can apply.")

'''
a student can mark some scholarships that
he/she is interested in.
those scholarships are shown in this page.
'''
def your_scholarships(request):
    return HttpResponse("marked scholarships.")
