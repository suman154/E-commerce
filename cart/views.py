from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()  # Call get_prods as a method
    quantities = cart.get_quants
    return render(request, 'cart_summary.html', {'cart_products': cart_products, "quantities":quantities})




def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        
        # Get cart quantity
        cart_quantity = cart.__len__()
        
        # Return JSON response with cart quantity
        response = JsonResponse({'qty': cart_quantity})
        return response
    
    # If the request method is not POST or the action is not 'post', return bad request response
    return JsonResponse({'error': 'Invalid request'}, status=400)

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

    cart.update(product=product_id, quantity=product_qty)

    response = JsonResponse({'qty':product_qty})
    return response
# return redirect(cart_summary)






def cart_delete(request):
    pass
