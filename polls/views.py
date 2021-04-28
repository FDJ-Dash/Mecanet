#from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
#from django.template import loader

# Create your views here.

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        Only display questions with choices in it.
        """
     #  List comprehensions provide a concise way to create lists.
     #  Example: squares = [x**2 for x in range(10)]
     #  A list comprehension consists of brackets containing an expression followed
     #  by a for clause, then zero or more for or if clauses.   
     
     #  Question.objects.filter(pk__in=[x.question.pk for x in Choice.objects.all()]) 
     #  for each choice in Choice.objects.all() put choice.question.pk in this list'. 
     #  The queryset will then return every Question for which there exists at least
     #  one related Choice.
        
        return Question.objects.filter(
            pub_date__lte=timezone.now() 
            ).filter(pk__in=[choice.question_id for choice in Choice.objects.all()]
            ).order_by('-pub_date')[:5] 
    
        #"""Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context, request))    
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)    
    #return HttpResponse("Hello, world. You're at the polls index.")

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
#    return render(request,'polls/detail.html', {'question' : question})
    #return HttpResponse("You're looking at question %s." % question_id)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})    
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))       
    #return HttpResponse("You're voting on question %s." % question_id)