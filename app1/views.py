from django.shortcuts import render, HttpResponseRedirect
from .models import Todo
from .forms import TodoForm
# Create your views here.

def home(request):

    if request.method == "POST":
          Fm = TodoForm(request.POST)

          if Fm.is_valid():
              Fm.save()
                
    else:
        Fm = TodoForm()

  


    taskshow = Todo.objects.all()


    return render(request, "app1/home.html", {"taskshow": taskshow, "Fm" : Fm})



def delete(request,id):
    obj = Todo.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect("/")



