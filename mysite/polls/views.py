from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_questions_list': latest_questions_list }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # get_object_or_404 calls get();
    # get_list_or_404 does the same, except using filter()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results for question {}.".format(question_id)
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question {}.".format(question_id))