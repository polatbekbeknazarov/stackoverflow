from django.urls import path
from questions.views import index

urlpatterns = [
    path('', index, name='index'),    
]


