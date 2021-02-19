from django.urls import path, include
from .import views
urlpatterns = [
    
    path('',views.index,name="index"),
    path('update_item/<str:pk>/',views.updateItem,name="update_item"),
    path('delete_item/<str:pk>/',views.deleteItem,name="delete_item"),
    #path('discounted_item/',views.discountItem,name="discounted_item")
]