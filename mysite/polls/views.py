from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request , 'polls/index.html' , context)


def detail(request, question_id):
     question = get_object_or_404(Question, pk=question_id)
     return render(request, 'polls/detail.html', {'question': question})

def results(request,question_id):
    response = "you are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("you are voting on question %s." % question_id)

def cal(request,var1,var2):
    ans=var1+var2
    response="the var1 is " + str(var1) + "  the var 2 is "  + str(var2) + "  the sum is " + str(ans)
    return HttpResponse(response)
