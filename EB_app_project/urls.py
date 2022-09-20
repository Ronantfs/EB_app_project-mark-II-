from django.contrib import admin
from django.urls import path
from EB_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.HomeView.as_view(), name='home'), #name='home' consistent with base template nav bar  
    path("questions/", views.QuestionsView, name = 'questions'), #name=''questions'' consistent with base template nav bar
    path("questions/create", views.CreateQuestionView.as_view(), name = 'create_question'), #name consistent with questions template link
    path("questions/<pk>/delete/", views.DeleteQuestionView.as_view(), name='delete_question'), 
    path("questions/<pk>/update/", views.UpdateQuestionView.as_view(), name='update_question'), 
]