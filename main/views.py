from django.shortcuts import render,redirect,get_object_or_404
from .models import Item

# Create your views here.
def home(request):
    return render(request, 'home.html')

def create(request): #Create - 객체 생성 부분
    if request.method == 'POST':
        item = Item()
        item.name = request.POST['name']
        item.store = request.POST['store']
        item.menu = request.POST['menu']
        item.option = request.POST['option']
        item.option = request.POST['price']

        item.save()
        return redirect('home')

def upadte(request): #Update - 객체 수정
    item = get_object_or_404(Item, pk = item_id)
    if request.method == 'POST':
        item = Item()
        item.name = request.POST['name']
        item.store = request.POST['store']
        item.menu = request.POST['menu']
        item.option = request.POST['option']
        item.option = request.POST['price']

        item.save()
        return redirect('home')
    else:
        return render(request,'update.html', {'items':item})

def delete(request, item_id): #Delete - 객체 삭제
    item = get_object_or_404(Item, pk = item_id)
    item.delete()

    return redirect('home')