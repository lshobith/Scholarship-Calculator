from django.shortcuts import render
from django.http import HttpResponse
from oauth2client import client, crypt
# Create your views here.


'''
this page has two types of login:
1. login with webmail.
2. login with gmail.
'''
def index(request):
    return render(request, 'app/login.html')

'''
an IITG student who has logged in using gmail
can view scholarships of IITG after verifying
with webmail ID and password in this page.

this verification is needed only once.
'''
def wverify(request):
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
def eligible(request):
    return render(request, 'app/eligible.html')

'''
a student can mark some scholarships that
he/she is interested in.
those scholarships are shown in this page.
'''
def your_scholarships(request):
    return HttpResponse("marked scholarships.")

'''
this is not a webpage but it verifies the gmail login
'''
def gverify(request):
    token = request.POST.get("idtoken", "")
    text = "me"
    try:
        idinfo = client.verify_id_token(token, "541322088910-o44t5oof2fr0hfjb4j4r3n27k67g2avb.apps.googleusercontent.com")
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise crypt.AppIdentityError("Wrong issuer.")
    except crypt.AppIdentityError:
        text = "none"
    return HttpResponse(text)
