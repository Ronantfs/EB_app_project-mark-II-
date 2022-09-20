from django.db import models
from taggit.managers import TaggableManager

class Exam(models.Model):
  title = models.CharField(unique=False, max_length=200)

  def __str__(self):
    return self.title

class Question(models.Model):
  name = models.CharField(unique=False, max_length=200)
  source = models.CharField(unique=False, max_length=200)
  #sections
  Section_choices = [("C","Core"),("S","Stats"),("M","Mechanics"),]
  section = models.CharField(default = "C", max_length=1, choices= Section_choices)
  publish_year = models.DateTimeField()
  AS_only = models.BooleanField(default = True)
  question_progress = models.IntegerField(default = 0)
  tags = TaggableManager()
  exams = models.ManyToManyField(Exam, blank=True)
  
  #image = models.ImageField(null =True, blank = True,upload_to='images/') #upload to: specifces which sub directory of media, images go to 
  #slug = models.SlugField(unique=True, default=uuid.uuid1)
  

  def get_absolute_url(self):
    return "/questions"

  def __str__(self):
    return f"{self.name}"
  
  class Meta: 
    ordering = ["question_progress"]









  