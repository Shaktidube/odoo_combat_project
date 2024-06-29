from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from OTS.models import *

def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())

def candidateRegistrationForm(request):
    res=render(request,'registration_form.html')
    return res
    

def candidateRegistration(request):
    if request.method == 'POST':
        username = request.POST['username']
        if Candidate.objects.filter(username=username).exists():
            userStatus = 1  # Username already exists
        else:
            candidate = Candidate(
                username=username,
                password=request.POST['password'],
                name=request.POST['name']
            )
            candidate.save()
            userStatus = 2  # Registration successful
    else:
        userStatus = 3  # Not a POST request
    
    context = {
        'userStatus': userStatus
    }
    return render(request, 'registration.html', context)



def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        candidate = Candidate.objects.filter(username=username,password=password)
        if len(candidate)==0:
            loginError = "Invalid Username or password"
            res = render(request,'login.html',{'loginError':loginError})
        else:
            request.session['username'] = candidate[0].username
            request.session['name'] = candidate[0].name
            res=HttpResponseRedirect("home")

    else:
        res=render(request,'login.html')
    
    return res


def candidateHome(request):
    if 'name' not in request.keys():
        res=HttpResponseRedirect(request,'login.html')

    else:
        res=render(request,'home.html')
    return res


def testPaper(request):
    pass


def calculateTestResult(request):
    pass


def testResultHistory(request):
    pass


def showTestResult(request):
    pass


def logoutView(request):
    pass


