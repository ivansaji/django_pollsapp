from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hi bro.... How you doing?")

def detail(request,question_id):
    return HttpResponse("You are looking at Question %s." % question_id)

def results(request,question_id):
    response = "you are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("you are voting on question %s." % question_id)

def cal(request,var1,var2):
    ans=var1+var2
    response="the var1 is " + str(var1) + "  the var 2 is "  + str(var2) + "  the sum is " + str(ans)
    return HttpResponse(response)
