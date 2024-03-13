from django.urls import path
from questions.views import index, quest_detail, add_question, questions_from_tag

urlpatterns = [
    path('', index, name='index'), 
    path('tag/<int:tag_id>/', questions_from_tag, name='tag_detail'),
    path('question/<slug:question_slug>/', quest_detail, name='quest_detail'),
    path('add_question/', add_question, name='add_question'),
]


