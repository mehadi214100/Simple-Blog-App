from django.shortcuts import render,redirect
from .models import Category
from .forms import categoryForm

def home(request):
    return render(request,"index.html")

def add_category(request):

    categories = Category.objects.all()
    total = categories.count()
    
    context = {
        "categories":categories,
        "total":total
    }

    if(request.method == 'POST'):
        form = categoryForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('add_category')
        
    else:
        form = categoryForm()

    return render(request,"add-category.html",context=context)

def delete_category(request,id):
    cat = Category.objects.get(id=id)
    cat.delete()
    return redirect('add_category')


def edit_category(request,id):
    cat = Category.objects.get(id=id)

    if(request.method == 'POST'):
        form = categoryForm(request.POST,instance=cat)

        if form.is_valid():
            form.save()
            return redirect('add_category')

    categories = Category.objects.all() 
    
    return render(request, "add-category.html", {'cat':cat,'total': categories.count(), 'categories': categories})