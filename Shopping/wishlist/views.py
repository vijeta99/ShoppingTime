from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
#from bs4 import BeautifulSoup
from .models import *
from .forms import *
# Create your views here.
def index(request):
    items=Item.objects.all()
    form=ItemForm()
    if request.method =='POST':
        form=ItemForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')


    context={'items':items,'form':form}
    return render(request,'wishlist/index.html',context)


def updateItem(request, pk):
    item=Item.objects.get(id=pk)
    form=ItemForm(instance=item)
    if request.method == 'POST':
        form=ItemForm(request.POST,instance=item)
        if form.is_valid:
            form.save()
        return redirect('/')
    context={'form':form}
    return render(request,'wishlist/update_item.html',context)


def deleteItem(request, pk):
    item=Item.objects.get(id=pk)
    context={'item':item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')


    return render(request,'wishlist/delete_item.html',context)
#def discountItem(request):
 #   items=Item.objects.all()
 #   headers= {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
 #  for item in items:
  #      URL =item.link
   #     page=requests.get(URL,headers=headers)
    #    soup=BeautifulSoup(page.content,'html.parser')
     #   #title=item.title
      #  price=soup.find(id="priceblock_ourprice").get_text()
       # converted_price=int(price[1])
        #if(converted_price < item.cost):
         #   item.status=True
    #context={'items':items}
    #return render(request,'wishlist/discountItem.html',context)

    



