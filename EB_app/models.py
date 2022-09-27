import email
from email.mime import image
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
  Section_choices = [("Core","Core"),("Stats","Stats"),("Mechanics","Mechanics"),]
  section = models.CharField(default = "Core", max_length=10, choices= Section_choices)
  tags = TaggableManager()
  AS_only = models.BooleanField(default = True)
  marks =  models.IntegerField(null = True, blank = True, default = 3)
  question_progress = models.IntegerField(default = 0)
  publish_year = models.DateTimeField()
  digital = models.BooleanField(default = False)
  image = models.ImageField(null = True, blank = True)

  #image method: 
  @property
  def imageURL(self): 
    try: 
      url = self.image.url
    except: 
      url = ''
    return url 
  

  def get_absolute_url(self):
    return "/questions"

  def __str__(self):
    return f"{self.name}"
  
  class Meta: 
    ordering = ["question_progress"]

## Exam order ##########################################
class ExamOrder(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
  complete = models.BooleanField(default=False)
  question_counter = models.IntegerField(null=True, blank=True)
  transaction_id = models.CharField(max_length=100, null=True)

 ## def __str__(self):
 ##  return str(self.id)

  @property
  def shipping(self):
    shipping = False
    examorderitems = self.examorderitem_set.all()
    for i in examorderitems:
      if i.question.digital == False:
        shipping = True
    return shipping
  
  @property
  def get_number_of_exam_qs(self):
    examorderitems = self.examorderitem_set.all()
    qc = 0
    for i in examorderitems: 
      qc += 1 
    return qc
  
  @property
  def get_total_marks(self):
    examorderitems = self.examorderitem_set.all()
    tm = 0
    for i in examorderitems: 
      tm += i.question.marks
    return tm
  
  @property
  def get_sections(self):
    examorderitems = self.examorderitem_set.all()
    sections = []
    for i in examorderitems: 
      if i.question.section not in sections: 
        sections.append(i.question.section)
    return sections
  
    
  @property
  def get_cart_items(self):
    examorderitems = self.examorderitem_set.all()
    return examorderitems 



## Exam order item ############################################
class ExamOrderItem(models.Model):
  question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
  exam_order = models.ForeignKey(ExamOrder, on_delete=models.SET_NULL, null=True)
  is_item_ordered= models.IntegerField(default=0, null=True, blank=True) 
  exam_question_number = models.IntegerField(null=True, blank=True)


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	examorder = models.ForeignKey(ExamOrder, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
  