from django.shortcuts import render,redirect,get_object_or_404
from .models import Item
from .models import User

# Create your views here.
def home(request):
    if request.method == 'POST':
        return redirect('payment')

    items = Item.objects.all()
    return render(request, 'home.html',{'items':items})

def menu(request, item_id): #menu.html
    store = get_object_or_404(Item, pk=item_id)
    menus = store.menu.split(',')
    return render(request,'menu.html',{'store':store,'menus':menus})
    #return render(request,'menu.html',{'menu':menu})

def product(request, item_id): #product.html
    products = User.objects.all()
    product = get_object_or_404(Item, pk=item_id)
    return render(request,'product.html', {'products':products,'product':product})

def payment(request): #product.html
    return render(request,'payment.html')

def update(request,item_id): #update.html
    update = get_object_or_404(Item,pk = item_id)
    return render(request,'update.html',{'update':update})

#---------------------------------------------------------------------
def create_item(request): #Create - 객체 생성 
    if request.method == 'POST':
        item = Item()
        item.usertype = request.POST['usertype']
        item.store = request.POST['store']
        item.menu = request.POST['menu']
        item.option = request.POST['option']
        item.price = request.POST['price']

        item.save()
        return redirect('home')

def update_item(request, item_id): #Update - 객체 수정
    item = get_object_or_404(Item, pk = item_id)
    if request.method == 'POST':
        item = Item()
        item.usertype = request.POST['usertype']
        item.store = request.POST['store']
        item.menu = request.POST['menu']
        item.option = request.POST['option']
        item.price = request.POST['price']

        item.save()
        return redirect('home')
    else:
        return render(request,'update_item', {'items':item})

def delete_item(request, item_id): #Delete - 객체 삭제
    item = get_object_or_404(Item, pk = item_id)
    item.delete()

    return redirect('home')

def create_user(request): #Create - 객체 생성 
    if request.method == 'POST':
        user = User()
        user.store = request.POST['store']
        user.menu = request.POST['menu']
        user.option = request.POST['option']
        user.price = request.POST['price']

        user.save()
        return redirect('home')

def update_user(request, user_id): #Update - 객체 수정
    item = get_object_or_404(Item, pk = user_id)
    if request.method == 'POST':
        user = User()
        user.store = request.POST['store']
        user.menu = request.POST['menu']
        user.option = request.POST['option']
        user.price = request.POST['price']

        user.save()
        return redirect('home')
    else:
        return render(request,'update_user', {'users':user})

def delete_user(request, user_id): #Delete - 객체 삭제
    user = get_object_or_404(Item, pk = user_id)
    user.delete()

    return redirect('home')