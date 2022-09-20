from django import forms
from .models import Question #import all models 

class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = "__all__"

