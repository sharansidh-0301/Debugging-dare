from django.shortcuts import render

def index(request):
    return render(request,'ddapp/index.html')

def easy(request):
    return render(request,'ddapp/easy.html')
def ide(request):
    return render(request,'ddapp/ide.html')
def problem(request):
    return render(request,'ddapp/problem.html')
def quiz(request):
    return render(request,'ddapp/quiz.html')
def quizpage(request):
    return render(request,'ddapp/quizpage.html')
def signup(request):
    return render(request,'ddapp/signup.html')



# Create your views here.
