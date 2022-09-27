from django.contrib import admin
from django.urls import path
from EB_app import views
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.HomeView.as_view(), name='home'), #name='home' consistent with base template nav bar 
    path("questions/", views.QuestionsView, name = 'questions'), #name=''questions'' consistent with base template nav bar
    path("questions/create", views.CreateQuestionView.as_view(), name = 'create_question'), #name consistent with questions template link
    path("questions/<pk>/delete/", views.DeleteQuestionView.as_view(), name='delete_question'), 
    path("questions/<pk>/update/", views.UpdateQuestionView.as_view(), name='update_question'), 
    path("update_item/", views.updateItem, name = "update_item"),
    path("cart/", views.cart, name = 'cart'),
    path("checkout/", views.checkout, name ="checkout"),
    path('process_order', views.processOrder, name = "process_order"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)