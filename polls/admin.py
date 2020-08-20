from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInLine(admin.StackedInline):
	"""docstring for C"""
	model=Choice
	extra=3
		
class QuestionAdmin(admin.ModelAdmin):
	"""docstring fos Q"""
	# fields=['pub_date','question_text']
	fieldsets=[
		(None,			{'fields':['question_text']}),
		('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
	]
	inlines=[ChoiceInLine]
	# list_display=('question_text','pub_date','was_published_recently')
	list_display=('question_text','pub_date','was_published_recently')
	list_filter=['pub_date']
	search_fields=['question_text']
		
admin.site.register(Question, QuestionAdmin)