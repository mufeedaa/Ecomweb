from django.shortcuts import render, redirect, get_object_or_404
from home.models import Category, Product
from django.contrib import messages
from .forms import ProductForm, CategoryForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/404/')
def admin_home(request):
    products = Product.objects.all() 
    return render(request, 'adminpanel/index.html',{'products': products})

@login_required(login_url='/404/')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect('admin_home')
    else:
        form = ProductForm()    
    form = ProductForm()

    return render(request, 'adminpanel/add_product.html', {'form': form})
    
@login_required(login_url='/404/')
def edit_product(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance = product) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('admin_home')
    else:
        form = ProductForm( instance = product) 

    return render(request, 'adminpanel/edit_product.html', {'form': form })
    
@login_required(login_url='/404/')
def delete_product(request, product_id): 
    product = get_object_or_404(Product, id = product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request,'Product deleted successfully')
        return redirect('admin_home')
    return render(request, 'adminpanel/delete_product.html', {'product':product})
  
@login_required(login_url='/404/')
def category_list(request): 
    categories = Category.objects.all().order_by('-id')
    return render(request, 'adminpanel/category_list.html', {'categories': categories}) 

@login_required(login_url='/404/')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New category is created!!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'adminpanel/add_category.html', {'form': form})        

@login_required(login_url='/404/')
def edit_category(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!!!')
            return redirect('category_list')
    else:
        form = CategoryForm(instance = category)
    return render(request, 'adminpanel/edit_category.html', {'form': form})  

@login_required(login_url='/404/')
def delete_category(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully')
    return redirect('category_list')

@login_required(login_url='/404/')
def sign_out(request):
    logout(request)
    return redirect('site_home')
