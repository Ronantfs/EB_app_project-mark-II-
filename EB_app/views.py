##import modules
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime


from .models import * #import all models
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

#cart: ---------------------------------------------
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        exam_order, created = ExamOrder.objects.get_or_create(customer=customer, complete=False) 
        questions = exam_order.examorderitem_set.all() #_set.all(): all exam_order_item objects linked to exam_order model 
    else:
        questions = []
    
    context = {'questions': questions}
    return render(request, 'EB_app/cart.html', context)

#add/remove from cart: ---------------------------------------------
def updateItem(request):
  print('request:' , request)
  questionId = request.POST.get('questionId') #links html tag with 
  action = request.POST.get('action')   #links html 
  print('Action:', action)
  print('Question:', questionId)

  customer = request.user.customer
  question = Question.objects.get(id=questionId)
  exam_order, created = ExamOrder.objects.get_or_create(customer=customer, complete=False)
  examOrderItem, created = ExamOrderItem.objects.get_or_create(exam_order= exam_order, question= question, exam_question_number = 1)
   

  if action == 'add': 
    examOrderItem.is_item_ordered = 1
    examOrderItem.save()
    ##number exam questions: 
    if  exam_order.question_counter == None:
        exam_order.question_counter = 0
    exam_order.question_counter += 1 
    print('number of questions in exam: ', exam_order.question_counter)
    exam_order.save()

  elif action == 'remove':
    examOrderItem.is_item_ordered = 0
    examOrderItem.save()
     ##number exam questions: 
    exam_order.question_counter -= 1 
    print('number of questions in exam: ', exam_order.question_counter)
    exam_order.save()

  if examOrderItem.is_item_ordered == 0: 
    examOrderItem.delete()

  return JsonResponse('Item was added', safe=False)

#checkout : --------------------------------------------------------------
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        examorder, created = ExamOrder.objects.get_or_create(customer=customer, complete=False) #examorder of log'd in user
        examorder_number_of_qs = examorder.get_number_of_exam_qs
        examorder_total_marks = examorder.get_total_marks
        examorder_sections = examorder.get_sections

        items = examorder.examorderitem_set.all() # items of log'd in user's examorder
        cartItems = examorder.get_cart_items # cartitems of log'd in user's examorder
        
    else: #Create empty cart for now for non-logged in user
        items = []
        examorder = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = examorder['get_cart_items']
    
    #link view function local varibles to html:
    context = {'items':items, 'examorder':examorder, 'cartItems':cartItems, 'number_of_qs':examorder_number_of_qs, 'total_marks':examorder_total_marks, 'author': customer, 'sections': examorder_sections} 
    return render(request, 'EB_app/checkout.html', context)



#views: 
def processOrder(request): 
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    if request.user.is_authenticated:
        customer = request.user.customer
        examorder, created = ExamOrder.objects.get_or_create(customer=customer, complete=False)
        examorder.transaction_id = transaction_id
    else:
        print('User is not logged in')
    
    examorder.save()
    
    if examorder.shipping == True: 
        ShippingAddress.objects.create(customer=customer,examorder=examorder,address=data['shipping']['address'],
        city=data['shipping']['city'],state=data['shipping']['state'],zipcode=data['shipping']['zipcode'],)

    return JsonResponse('Order subbmitted..', safe=False)




