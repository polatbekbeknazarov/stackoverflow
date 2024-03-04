from django.shortcuts import render

from questions.models import Question

def index(request):
    questions = Question.objects.all()

    context = {
        'questions': questions,
    }

    return render(request, 'questions/index.html', context)
