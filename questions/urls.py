from django.urls import path
from . import views

urlpatterns = [
    path('addQuestion/' ,views.new_question, name="Adding question" ),
    path('answer/<int:id>', views.answer_question, name="Answer the Question"),
    path('like/<int:id>', views.like_question, name="Like the Question" ),
    path('dislike/<int:id>', views.dislike_question, name="Dislike the Question" ),
]

