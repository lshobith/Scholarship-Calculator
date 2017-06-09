from django.shortcuts import render
from django.http import HttpResponse
from oauth2client import client, crypt
from .models import Person, PersonForm

'''
this page has two types of login:
1. login with webmail.
2. login with gmail.
'''
def login(request):
    return render(request, 'app/login.html')

'''
an IITG student who has logged in using gmail
can view scholarships of IITG after verifying
with webmail ID and password in this page.

this verification is needed only once.
'''
def wverify(request):
    if not request.session.__contains__('userid'):
        return HttpResponse("you are not logged in!")

    return render(request, 'app/wverify.html')

'''
students enter their details in this page.
'''
def profile(request):
    if not request.session.__contains__('userid'):
        return HttpResponse("you are not logged in!")
    person = Person.objects.get(gmail_id=request.session['userid'])
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm(instance=person)

    return render(request, 'app/profile.html', {'form': form})

'''
all scholarships a student is eligible to
apply are shown in this page.
'''
def eligible(request):
    if not request.session.__contains__('userid'):
        return HttpResponse("you are not logged in!")

    return render(request, 'app/eligible.html')

'''
a student can mark some scholarships that
he/she is interested in.
those scholarships are shown in this page.
'''
def saved(request):
    if not request.session.__contains__('userid'):
        return HttpResponse("you are not logged in!")

    return render(request, 'app/saved.html')

'''
this is for logout
'''
def glogout(request):
    if not request.session.__contains__('userid'):
        return HttpResponse("You're not logged in!")
    try:
        del request.session['userid']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

'''
this is not a webpage but it verifies the gmail login
'''
def gverify(request):
    token = request.POST['idtoken']
    text = ''
    try:
        idinfo = client.verify_id_token(token, "541322088910-o44t5oof2fr0hfjb4j4r3n27k67g2avb.apps.googleusercontent.com")
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise crypt.AppIdentityError("Wrong issuer.")
    except crypt.AppIdentityError:
        text = 'Sign in failed'
    else:
        request.session['userid'] = idinfo['sub']
        text = 'Signed in as: ' + idinfo['sub']
        if not Person.objects.filter(gmail_id=request.session['userid']).exists():
            new_user = Person(gmail_id=request.session['userid'])
            new_user.save()
            text = '(new user)' + text
    return HttpResponse(text)