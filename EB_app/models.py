import email
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

#############Models: 
class Customer(models.Model):
  user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
  name = models.CharField(max_length= 200, null = True)
  email = models.CharField(max_length= 200)

  def __str__(self): 
    return self.name

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
  #exams = models.ManyToManyField(ExamOrder, blank=True)
  
  #image = models.ImageField(null =True, blank = True,upload_to='images/') #upload to: specifces which sub directory of media, images go to 
  #slug = models.SlugField(unique=True, default=uuid.uuid1)
  

  def get_absolute_url(self):
    return "/questions"

  def __str__(self):
    return f"{self.name}"
  
  class Meta: 
    ordering = ["question_progress"]


class ExamOrder(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
  complete = models.BooleanField(default=False)
  transaction_id = models.CharField(max_length=100, null=True)
  def __str__(self):
    return str(self.id)

class ExamOrderItem(models.Model):
  question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
  exam_order = models.ForeignKey(ExamOrder, on_delete=models.SET_NULL, null=True)
  quantity = models.IntegerField(default=0, null=True, blank=True)




  