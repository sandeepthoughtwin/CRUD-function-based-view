from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
from .forms import Studentforms
from django import forms
from django.shortcuts import (get_object_or_404,
                              redirect)

# from information import forms

# Create your views here.
def create_view(request):
    if request.method == 'POST':
        form = Studentforms(request.POST or None)
        if form.is_valid():
            form.save()
            print("Succes")
            return redirect('list')
            
    
    form = Studentforms()
    return render(request, "create_view.html",{'form':form})

def list_view(request):
    dic = {}
 
    dic["student_list"] = Student.objects.filter(roll_num =100)
   
         
    return render(request, "list_view.html", dic)

def update_view(request,id):
    dic ={}
    obj = get_object_or_404(Student, id = id)
    form = Studentforms(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/list")

    dic["form"] = form
    return render(request, "update_view.html", dic) 

def delete_view(request, id):
    dic ={}
    obj = get_object_or_404(Student, id = id)
    if request.method =="POST":
        obj.delete()
        return redirect("/list")
    return render(request, "delete_view.html", dic)    
