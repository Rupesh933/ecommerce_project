from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')

    # paginator 
    paginator = Paginator(products, 2) # 6 products per page
    page = request.GET.get('page') # get the page number from the url (?page=2)
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products' : paged_products,
        'product_count' : product_count,
    }
    return render(request, 'store/store.html', context)

def product_details(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        # this code is for when an item is already in cart then show already in cart
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        # return HttpResponse(in_cart)
    except Exception as e:
        raise e
    
    context = {
        'single_product' : single_product,
        'in_cart' : in_cart,
        
    }
    return render(request, 'store/product_details.html', context)

    path('search/', views.search, name='search'),

def search(request):
    if 'keyword' in request.GET: # if there is a keyword in the url (?keyword=iphone)
        keyword = request.GET['keyword'] # get the keyword from the url
        if keyword: # if the keyword is not empty
            #  search for products that contain the keyword in the description (case insensitive)
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products' : products,
        'product_count' : product_count
    }
    return render(request, 'store/store.html', context)
    # return HttpResponse('<h1>search page</h1>')