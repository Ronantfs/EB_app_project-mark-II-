##import modules
from django.shortcuts import render
from .models import Question #import all models
from .forms import QuestionForm #import all forms 
from .filters import QuestionFilter

#import generic views for CRUD
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 

#import for success url in delete views 
from django.urls import reverse_lazy


#home view as class-based view: 

class HomeView(TemplateView):
    template_name = "EB_app/home.html"     #how to add context? 

#Question CRUD views: ---------------------------------------------
def QuestionsView(request): 

    questions = Question.objects.all()
    question_filter = QuestionFilter(request.GET, queryset= questions) #applies QuestionFilter to query set 
    #add_to_exam = Add_to_ExamFilter(request.GET, queryset= question_filter) #applies Add_to_ExamFilter to query set
    
    #apply second filter to question_filter query set 

    context ={
        'questions': questions,
        'question_filter': question_filter
    }
    return render(request, "EB_app/questions.html", context)
    

class CreateQuestionView(CreateView):
    model = Question 
    template_name = "EB_app/question_create.html"
    form_class = QuestionForm

class DeleteQuestionView(DeleteView):
    model = Question
    template_name = "EB_app/question_delete.html"
    success_url = reverse_lazy('questions')

class UpdateQuestionView(UpdateView):
    model = Question 
    template_name = "EB_app/question_update.html"
    form_class = QuestionForm
    success_url = reverse_lazy('questions')






