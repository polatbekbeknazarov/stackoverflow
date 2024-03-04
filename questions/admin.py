from django.contrib import admin
from questions.models import Question, Tag


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'closed', 'created_at', 'updated_at',)
    list_display_links = ('id', 'user')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    