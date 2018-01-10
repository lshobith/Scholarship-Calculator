from django.shortcuts import render
from django.http import HttpResponse
from oauth2client import client, crypt
from django.db.models import Q
from .models import Person, Scholarship
from .forms import PersonForm, WebmailVerifyForm
import poplib
import re

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
    elif not Person.objects.filter(gmail_id=request.session['userid']).exists():
        try:
            del request.session['userid']
        except KeyError:
            pass
        return HttpResponse("Invalid User, Please login again!")

    if request.method == 'POST':
        form = WebmailVerifyForm(request.POST)
        if form.is_valid():
            try:
                serv = poplib.POP3_SSL( request.POST['server'] , '995' )
                status_username = serv.user( request.POST['webmail_id'] )
                status_password = serv.pass_( request.POST['password'] )
                '''
                if status_username == '' and status_password == '': #TODO
                    similar_users = Person.objects.filter() #TODO
                    current_user = Person.objects.get(gmail_id=request.session['userid']) #TODO
                '''
            except Exception:
                pass
    else:
        form = WebmailVerifyForm()

    return render(request, 'app/wverify.html', {'form': form})

'''
students enter their details in this page.
'''
def profile(request):
    if not request.session.__contains__('userid'):
        return HttpResponse("you are not logged in!")
    elif not Person.objects.filter(gmail_id=request.session['userid']).exists():
        try:
            del request.session['userid']
        except KeyError:
            pass
        return HttpResponse("Invalid User, Please login again!")
    current_user = Person.objects.get(gmail_id=request.session['userid'])
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm(instance=current_user)

    return render(request, 'app/profile.html', {'form': form})

'''
all scholarships a student is eligible to
apply are shown in this page.
'''
def eligible(request):
    if not request.session.__contains__('userid'):
        return HttpResponse("you are not logged in!")
    elif not Person.objects.filter(gmail_id=request.session['userid']).exists():
        try:
            del request.session['userid']
        except KeyError:
            pass
        return HttpResponse("Invalid User, Please login again!")
    current_user = Person.objects.get(gmail_id=request.session['userid'])
    marked_scholarship_list = current_user.marked_scholarships.all()
    scholarship_list = Scholarship.objects.all()

    # FILTER START
    '''
    if current_user.iitg_student == 'N':
        scholarship_list = Scholarship.objects.filter(
            iitg_scholarship = 'N'
        )
    else:
        scholarship_list = Scholarship.objects.all()
    if current_user.citizen_india == 'N':
        scholarship_list = scholarship_list.filter(
            eligible_nations = 'ALL'
        )
    my_filter = {}
    if not (current_user.education == 'E' or current_user.education == 'NAOT'):
        req_string = 'level_' + current_user.education
        my_filter[req_string] = True
    if not (current_user.extra_education == 'E' or current_user.extra_education == 'NAOT'):
        req_string = 'level_' + current_user.extra_education
        my_filter[req_string] = True
    if not (current_user.religion == 'E' or current_user.religion == 'NAOT'):
        my_filter[current_user.religion] = True
    if not (current_user.category == 'E' or current_user.category == 'NAOT'):
        my_filter[current_user.category] = True
    if not (current_user.workers == 'E' or current_user.workers == 'NAOT'):
        my_filter[current_user.workers] = True
    if not (current_user.armed == 'E' or current_user.armed == 'NAOT'):
        my_filter[current_user.armed] = True

    if not current_user.gender == 'E':
        my_filter[current_user.gender] = True

    scholarship_list = scholarship_list.filter(**my_filter)

    if not current_user.annual_income is None:
        scholarship_list = scholarship_list.filter(Q(maximum_income_annual__gte = current_user.annual_income) | Q(maximum_income_annual = None))
    if not current_user.monthly_income is None:
        scholarship_list = scholarship_list.filter(Q(maximum_income_monthly__gte = current_user.monthly_income) | Q(maximum_income_monthly = None))
    if not current_user.lump_sum is None:
        scholarship_list = scholarship_list.filter(Q(maximum_lump_sum_or_installments__gte = current_user.lump_sum) | Q(maximum_lump_sum_or_installments = None))
    if not current_user.current_cpi is None:
        scholarship_list = scholarship_list.filter(Q(minimum_cpi__lte = current_user.current_cpi) | Q(minimum_cpi = None))
    if not current_user.marks_percentage is None:
        scholarship_list = scholarship_list.filter(Q(minimum_percent__lte = current_user.marks_percentage) | Q(minimum_percent = None))
    if not current_user.disability_percent is None:
        scholarship_list = scholarship_list.filter(Q(minimum_disability_percent__lte = current_user.disability_percent) | Q(minimum_disability_percent = None))
    '''
    # FILTER END

    content = {
        'scholarship_list': scholarship_list,
        'marked_scholarship_list': marked_scholarship_list
    }

    return render(request, 'app/eligible.html', content)

'''
a student can mark some scholarships that
he/she is interested in.
those scholarships are shown in this page.
'''
def saved(request):
    if not request.session.__contains__('userid'):
        return HttpResponse("you are not logged in!")
    elif not Person.objects.filter(gmail_id=request.session['userid']).exists():
        try:
            del request.session['userid']
        except KeyError:
            pass
        return HttpResponse("Invalid User, Please login again!")
    current_user = Person.objects.get(gmail_id=request.session['userid'])
    scholarship_list = current_user.marked_scholarships.all()
    content = {'scholarship_list': scholarship_list}

    return render(request, 'app/saved.html', content)

'''
this page is displayed in case of first time login
'''
def fxprofile(request):
    if not request.session.__contains__('userid'):
        return HttpResponse("you are not logged in!")
    elif not Person.objects.filter(gmail_id=request.session['userid']).exists():
        try:
            del request.session['userid']
        except KeyError:
            pass
        return HttpResponse("Invalid User, Please login again!")

    current_user = Person.objects.get(gmail_id=request.session['userid'])
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm(instance=current_user)
    return render(request, 'app/fxprofile.html', {'form': form})

'''
this page is displayed in case of first time login
'''
def fxwver(request):
    if not request.session.__contains__('userid'):
        return HttpResponse("you are not logged in!")
    elif not Person.objects.filter(gmail_id=request.session['userid']).exists():
        try:
            del request.session['userid']
        except KeyError:
            pass
        return HttpResponse("Invalid User, Please login again!")

    if request.method == 'POST':
        form = WebmailVerifyForm(request.POST)
        if form.is_valid():
            try:
                serv = poplib.POP3_SSL( request.POST['server'] , '995' )
                status_username = serv.user( request.POST['webmail_id'] )
                status_password = serv.pass_( request.POST['password'] )
                '''
                if status_username == '' and status_password == '': #TODO
                    similar_users = Person.objects.filter() #TODO
                    current_user = Person.objects.get(gmail_id=request.session['userid']) #TODO
                '''
            except Exception:
                pass
    else:
        form = WebmailVerifyForm()

    return render(request, 'app/fxwver.html', {'form': form})

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
        text = 'old user'
        if not Person.objects.filter(gmail_id=request.session['userid']).exists():
            new_user = Person(gmail_id=request.session['userid'])
            new_user.save()
            text = 'new user'
    return HttpResponse(text)

def mark(request):
    if not request.session.__contains__('userid'):
        return HttpResponse("you are not logged in!")
    elif not Person.objects.filter(gmail_id=request.session['userid']).exists():
        try:
            del request.session['userid']
        except KeyError:
            pass
        return HttpResponse("Invalid User, Please login again!")
    if request.method == 'POST':
        number = int(re.search(r'\d+', request.POST['scholarship_id']).group())
        keyword = ''.join([i for i in request.POST['scholarship_id'] if not i.isdigit()])
        current_user = Person.objects.get(gmail_id=request.session['userid'])
        requested_scholarship = Scholarship.objects.get(id=number)
        if keyword == 'save':
            try:
                current_user.marked_scholarships.add(requested_scholarship)
            except Exception:
                return HttpResponse('reload your page and try again')
            return HttpResponse('save ok')
        elif keyword == 'remove':
            try:
                current_user.marked_scholarships.remove(requested_scholarship)
            except Exception:
                return HttpResponse('reload your page and try again')
            return HttpResponse('remove ok')
        else:
            return HttpResponse('try again')
