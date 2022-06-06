from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .form import ContactForm, SnippetForm


# Create your views here.
def contact(request):
    if request.method =='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name =form.cleaned_data['name']
            email =form.cleaned_data['email']
            roles =form.cleaned_data['roles']
            spirit_animal =form.cleaned_data['spirit_animal']
            





    form =ContactForm()
    return render(request,'form.html',{'form':form})

    
def snippet_detail(request):
    if request.method =='POST':
        form=SnippetForm(request.POST)
        if form.is_valid():
            print("valid")
            





    form =SnippetForm()
    return render(request,'form.html',{'form':form})
