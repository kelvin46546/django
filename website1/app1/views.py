from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':""}
    return render(request,'index.html',context=my_dict)

def help(request):
    helpdict = {'help_insert':''}
    return render(request, 'app2/help.html',context=helpdict)

def intro(request):
    introdict = {' intro_page ':''}
    return render(request, 'app3/intro.html',context=introdict)

def epic(request):
    epicdict = {' epic_page ':''}
    return render(request, 'app4/epic.html',context=epicdict)
