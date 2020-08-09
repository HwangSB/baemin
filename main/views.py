from django.shortcuts import render,redirect,get_object_or_404
from .models import Store, User

# Create your views here.
def home(request):
    if request.method == 'POST':
        return redirect('payment')

    context = {
        'stores': Store.objects.all()
    }

    return render(request, 'home.html', context)

def menu(request, store_id): #menu.html
    store = get_object_or_404(Store, pk=store_id)
    menus = store.menu.split('\r\n')
    menu_list = []
    for menu in menus:
        data = menu.split(':')
        menu_list.append((data[0], data[1]))
    return render(request, 'menu.html', {'store': store, 'menus': menu_list})

def product(request, store_id, menu_id): #product.html
    products = User.objects.all()
    store = get_object_or_404(Store, pk = store_id)
    product_object = get_object_or_404(Store, pk=store_id)
    product = product_object.menu.split('\r\n')[menu_id - 1].split(':')[0]
    product_price = product_object.menu.split('\r\n')[menu_id - 1].split(':')[1]
    total = 0
    for price in products:
        total += price.price
    return render(request,'product.html', {'store':store,'products':products,'product':product,'product_price':product_price,'total':total})

def payment(request): #product.html
    products = User.objects.all()
    total = 0
    for price in products:
        total += price.price
    return render(request,'payment.html',{'products':products,'total':total})

def order(request): #product.html
    products = User.objects.all()
    total = 0
    for price in products:
        total += price.price
    return render(request,'order.html',{'products':products,'total':total})

def update(request,store_id): #update.html
    update = get_object_or_404(Store,pk = store_id)
    return render(request,'update.html', {'update':update})

#---------------------------------------------------------------------
def create_item(request): #Create - 객체 생성 
    if request.method == 'POST':
        store = Store()
        store.usertype = request.POST['usertype']
        store.store = request.POST['store']
        store.menu = request.POST['menu']
        store.option = request.POST['option']
        store.price = request.POST['price']

        store.save()
        return redirect('home')

def update_item(request, store_id): #Update - 객체 수정
    store = get_object_or_404(Store, pk = store_id)
    if request.method == 'POST':
        store = Store()
        store.usertype = request.POST['usertype']
        store.store = request.POST['store']
        store.menu = request.POST['menu']
        store.option = request.POST['option']
        store.price = request.POST['price']

        store.save()
        return redirect('home')
    else:
        return render(request, 'update.html', {'store':store})

def delete_item(request, store_id): #Delete - 객체 삭제
    store = get_object_or_404(Store, pk = store_id)
    store.delete()

    return redirect('home')

def create_user(request): #Create - 객체 생성 
    if request.method == 'POST':
        user = User()
        user.store = request.POST['store']
        user.menu = request.POST['menu']
        user.option = request.POST['option']
        user.price = request.POST['price']

        user.save()
        return redirect('order')

def update_user(request, user_id): #Update - 객체 수정
    item = get_object_or_404(User, pk = user_id)
    if request.method == 'POST':
        user = User()
        user.store = request.POST['store']
        user.menu = request.POST['menu']
        user.option = request.POST['option']
        user.price = request.POST['price']

        user.save()
        return redirect('order')
    else:
        return render(request,'update_user', {'users':user})

def delete_user(request, user_id): #Delete - 객체 삭제
    user = get_object_or_404(User, pk = user_id)
    user.delete()

    return redirect('order')