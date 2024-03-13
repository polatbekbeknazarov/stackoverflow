from django.shortcuts import render, get_object_or_404, redirect

from questions.models import Question
from questions.forms import AddQuestionFrom

def index(request):
    questions = Question.objects.all()

    context = {
        'questions': questions,
    }

    return render(request, 'questions/index.html', context)

def quest_detail(request, question_slug):
    question = get_object_or_404(Question, slug=question_slug)

    context = {
        'question': question,
    }

    return render(request, 'questions/question_detail.html', context)


def questions_from_tag(request, tag_id):
    questions = Question.objects.filter(tag=tag_id)

    context = {
        'questions': questions,
    }

    return render(request, 'questions/index.html', context)


def add_question(request):
    form = AddQuestionFrom()

    if request.method == 'POST':
        form = AddQuestionFrom(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            form.save_m2m()

            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'questions/add_question.html', context)
