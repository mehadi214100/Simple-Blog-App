from django.shortcuts import render,redirect
from .models import Category,Author,Post
from .forms import categoryForm,authorForm,postForm

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

def add_author(request):

    if(request.method =='POST'):
        form = authorForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('add_author')
            
    else:
        form = authorForm()

    authors = Author.objects.all()

    return render(request,'add-author.html',{"authors":authors})

def edit_author(request,id):
    author = Author.objects.get(id=id)

    if(request.method =='POST'):
        form = authorForm(request.POST,request.FILES,instance=author)
        if(form.is_valid()):
            form.save()
            return redirect('add_author')
            
    else:
        form = authorForm()
    
    authors = Author.objects.all()

    return render(request,'add-author.html',{"authors":authors,"author":author})

def delete_author(request,id):
    auth = Author.objects.get(id=id)
    auth.delete()
    return redirect('add_author')

def add_post(request):

    if(request.method=='POST'):
        form = postForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('home')
    else:
        form = postForm()
    
    authors = Author.objects.all()
    categories = Category.objects.all()

    context = {
        'form': form,
        'authors': authors,
        'categories': categories
    }
    return render(request, 'add-post.html', context)

