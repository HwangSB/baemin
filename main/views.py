from django.shortcuts import render,redirect,get_object_or_404
from .models import Item

# Create your views here.
def home(request):
    if request.method == 'POST':
        return redirect('payment')

    items = Item.objects.all()
    return render(request, 'home.html',{'items':items})

def menu(request, item_id): #menu.html
    store = get_object_or_404(Item, pk=item_id)
    menus = menu.menu.split(',')
    # 불싸이버거:5000,싸이버거:6000
    return render(request,'menu.html',{'store':store,'menus':menus})
    #return render(request,'menu.html',{'menu':menu})

def product(request, item_id): #product.html
    product = get_object_or_404(Item, pk=item_id)
    return render(request,'product.html', {'product':product})

def payment(request): #product.html
    return render(request,'payment.html')

def update(request,item_id): #update.html
    update = get_object_or_404(Item,pk = item_id)
    return render(request,'update.html',{'update':update})

#---------------------------------------------------------------------
def create(request): #Create - 객체 생성 
    if request.method == 'POST':
        item = Item()
        item.usertype = request.POST['usertype']
        item.store = request.POST['store']
        item.menu = request.POST['menu']
        item.option = request.POST['option']
        item.price = request.POST['price']

        item.save()
        return redirect('home')

def update(request, item_id): #Update - 객체 수정
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
        return render(request,'update.html', {'items':item})

def delete(request, item_id): #Delete - 객체 삭제
    item = get_object_or_404(Item, pk = item_id)
    item.delete()

    return redirect('home')