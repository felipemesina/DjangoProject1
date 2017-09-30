from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
from models import Travel
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'exam/index.html')


def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    return redirect('/success')


def login_view(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    return redirect('/home')


def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'exam/success.html', context)


def home(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'trip': Travel.objects.all(),
    }
    return render(request, 'exam/home.html', context)



def travel(request):
    return render(request, 'exam/add_travel.html')



def add_travel(request):
    errs = Travel.objects.validate_travel(request.POST)
    user = User.objects.get(id=request.session['user_id'])
    if errs:
        for e in errs:
            messages.error(request, e)
        return redirect('/travel/')

    else:
        Travel.objects.create(
        user = user,
        destination = request.POST['destination'],
        desc = request.POST['desc'],
        date_from = request.POST['date_from'],
        date_to = request.POST['date_to'],
    )
    return redirect('/home')
