from django.shortcuts import render, redirect
from questions.models import Question, User
from datetime import date

def new_question(request):
    if request.POST:
        questions = request.POST["question"]
        username = request.user.username
        posted_date = date.today()
        
        ques = Question(qes= questions, username=username, posted_date= posted_date,up_count=0,downvote_count=0)
        ques.save()
        
        return redirect('Home')
    
    return render(request, 'addQuestion.html')

def answer_question(request, id):
    try:
        old_data = Question.objects.get(pk=id)
    except:
        return redirect("Home")
    
    context = {
        "question" : old_data.qes
    }
    if request.POST:
        answer = request.POST['answer']
        answer_by = request.POST["ansuser"]
        
        old_data.ans = answer
        old_data.answer_by = answer_by
        
        old_data.save()
        
        return redirect('Home')
    
    return render(request, "addAnswer.html", context)

def like_question(request, id):
    try:
        question = Question.objects.get(pk=id)
    except:
        return redirect("Home")
    
    if question:
        question.up_count += 1
        question.save()
        
        return redirect("Home")
    
def dislike_question(request, id):
    try:
        question = Question.objects.get(pk=id)
    except:
        return redirect("Home")
    
    if question:
        question.downvote_count += 1
        question.up_count -= 1
        question.save()
        
        return redirect("Home")

