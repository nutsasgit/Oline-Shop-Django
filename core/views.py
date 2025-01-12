from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.shortcuts import get_object_or_404

# Create your views here.

def productlistView(request):

    products = Product.objects.all()

    context = {
        'object_list': products,
    }
    template_name = 'core/productList.html'

    return render(request,template_name, context)

def createProductView(request):

    print('test create view ======',request.POST)
    if request.POST:
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        stock = data.get('stock')
        is_active = data.get('is_active')

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            is_active=True
        )

        return redirect('product-list')


    template_name = 'core/createProduct.html'
    return render(request, template_name,{})

def productDetailView(request, product_id):
    template_name = 'core/productDetail.html'

    product = Product.objects.get(id=product_id)

    print('datrigerdes............',product_id)


    context = {
        'product': product
    }
    return render(request, template_name,context)

def productUpdateView(request, product_id):
    template_name = 'core/productUpdate.html'
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance=product)
    print('product-update View.....', product_id)

    if request.method =="POST":
        form=ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        else:
            form = ProductForm(instance=product)


    context = {
        'product': product,
        'form': form
    }
    return render(request, template_name, context)

def productDeleteView(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    template_name = 'core/productDelete.html'

    if request.method == "POST":
        product.delete()
        return redirect('product-list')
    context = {
        'product': product,
    }

    return render (request, template_name, context)