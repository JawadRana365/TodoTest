from django.shortcuts import render,redirect
from django.contrib import messages

## import todo form and models

from .forms import TodoForm
from .models import Todo,User,Category

###############################################



def index(request):
    if request.session.has_key('username'):
        item_list = Todo.objects.order_by("-priority")
        if request.method == "POST":
            form = TodoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('todo')
        form = TodoForm()
        page = {
            "forms" : form,
            "list" : item_list,
            "user" : User.objects.all(),
            "category" : Category.objects.all(),
            "title" : "TODO LIST",
            "session": request.session
        }
        return render(request,'todo/index.html',page)
    else:
        return render(request, 'todo/login.html')

### function to remove item , it recive todo item id from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request,"item removed !!!")
    return redirect('todo')

def update(request):
    Todo.objects.filter(pk=request.POST.get("id","")).update(title=request.POST.get("title","").strip(),details=request.POST.get("details","").strip(),priority=request.POST.get("priority",""),completed=request.POST.get("completed",""),category_id=request.POST.get("category",""))
    return redirect('todo')
def login(request):
    if(request.method == "POST"):
        user = User.objects.filter(userName = request.POST.get("username",""),password = request.POST.get("password","")).count()
        if user > 0 :
            request.session['username'] = request.POST.get("username", "")
            return redirect('todo')
        else:
            return render(request, 'todo/login.html')
    else:
        return render(request, 'todo/login.html')


def logout(request):
    del request.session['username']
    return redirect('todo')

def signup(request):
    if "username" in request.POST:
        User(userName=request.POST.get("username",""),password=request.POST.get("password","")).save()
        request.session['username'] = request.POST.get("username","")
        return redirect('todo')
    else:
        return render(request, 'todo/signup.html')
def category(request):
    Category(title=request.POST.get("title","")).save()
    return  redirect('todo')