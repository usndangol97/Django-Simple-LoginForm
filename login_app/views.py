from django.shortcuts import render
from django.http import HttpResponse
from .forms import createUserForm

# Create your views here.
def  index(request):
    form = createUserForm()
    context = {'form':form}
    return render(request,'login_app/index.html',context)

def  login_page(request):
    return render(request,'login_app/login.html')
