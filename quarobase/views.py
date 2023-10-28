from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from questions.models import Question

@login_required
def home(request):
    questions_data = Question.objects.all().values()
    
    context = {
        "questions" : questions_data
    }
    return render(request, 'home.html', context)

