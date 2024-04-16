from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem
from .tasks import order_created
from django.contrib.auth.decorators import login_required

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():

            order = form.save()

            for item in cart:
                new_order = OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'], profile=request.user.profile)
                new_order.save()
            cart.clear()

            order_created.delay(order.id)

            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()    

    return render(request, 'orders/order/create.html', {'form': form, 'cart':cart})        

@login_required
def history(request):
    orders = Order.objects.filter(items__profile=request.user.profile).order_by('-id').distinct('id')
    return render(request, 'orders/history.html', {'orders': orders})
