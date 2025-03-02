from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('easy',views.easy,name='easy'),
    path('ide',views.ide,name='ide'),
    path('problem',views.problem,name='problem'),
    path('quiz',views.quiz,name='quiz'),
    path('quizpage',views.quizpage,name='quizpage'),
    path('signup',views.signup,name='signup'),
]
