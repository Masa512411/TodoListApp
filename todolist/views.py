from django.shortcuts import render
from .models import Todo
# Create your views here.
def index(request):
    todo = Todo.objects.all()
    return render(request, 'todolist/index.html',{'tasks':todo})
    #return HttpResponse("<h1>Hello, world. You're at the todolist index.</h1>")