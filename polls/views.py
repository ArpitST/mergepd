from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question

# Create your views here.
class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'
	# context_object_name = 'question'

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model=Question
	template_name='polls/results.html'
				
						
	# docstring fos IndexView"generic.ListViewf __init__(self, arg):
	# 	supes IndexView,generic.ListView.__init__()
	# 	self.arg = arg

# def index(request):
# 	latest_question_list=Question.objects.order_by('-pub_date')[:5]
# 	# template=loader.get_template('polls/index.html')
# 	context={'latest_question_list':latest_question_list}
# 	# output=','.join([q.question_text for q in latest_question_list])
# 	# return HttpResponse(template.render(context,request))
# 	# return HttpResponse(output)
# 	# return HttpResponse("Hello, world. You're at the polls index.")
# 	return render(request,'polls/index.html',context)

# def detail(request,question_id):
# 	question=get_object_or_404(Question, pk=question_id)
# 	try:
# 		question=Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question DoesNotExist")	
# 	return render(request,'polls/detail.html',{'question':question})
# 	return HttpResponse("You're looking at question %s." % question_id)

# def results(request,question_id):
# 	question=get_object_or_404(Question, pk=question_id)
# 	return render(request,'polls/results.html',{'question':question})
# 	# response="You're looking at the results of question %s."	
	# return HttpResponse(response % question_id)

def vote(request,question_id):
	question=get_object_or_404(Question, pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request,'polls/detail.html',{'question':question, 'error_message':"You didn't select a choice"})
	else:
		selected_choice.votes+=1
		selected_choice.save()
	# return HttpResponse("You're voting on question %s." % question_id)	
		return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(request, question_id):
	question=get_object_or_404(Question, pk=question_id)
	return render(request,'polls/results.html',{'question':question})
