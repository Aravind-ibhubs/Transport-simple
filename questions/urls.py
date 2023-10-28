from django.urls import path
from . import views

urlpatterns = [
    path('addQuestion/' ,views.new_question, name="Adding question" ),
    path('answer/<int:id>', views.answer_ques, name="Answer the Question"),
]

