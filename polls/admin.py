from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # Create separate sections on the question creation page
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # Fields to show on the question list page
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Create a filter for publication date on the question list page
    list_filter = ['pub_date']
    # Add the ability to search questions on the question list page
    search_fields = ['question_text']
    
    # Show the choice details on the question creation page
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
