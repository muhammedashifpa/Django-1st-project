from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect, render
from django.http.response import HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages

class profile:
    name:str
    login_status:bool
    username :str
    password:str
    login_status = False

profile1 = profile()
profile1.name= 'Muhammed Ashif'
profile1.username = 'ashif_mohdz'
profile1.password = '   '
Anonymous = profile()

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    print('\n\n***login requested***\n\n')
    if request.session.has_key('is_logged'):
        return redirect('home')
    return render(request,'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == profile1.username and password == profile1.password:
            request.session['is_logged'] = True
            print('\n\n submited \n\n')
            return redirect('home')
        else:
            messages.error(request,'Invalid authentication...')
    return redirect('login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.session.has_key('is_logged'):
    # if request.session['is_logged']==True:
        return render(request,'home.html',{'profile1':profile1})
    return redirect('login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    if request.session.has_key('is_logged'):
        print('\n\n***Session deleted***\n\n')
        del request.session['is_logged']
    return redirect('login')
    



    
