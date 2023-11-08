from django.shortcuts import render
from calciapp.forms import Fields
# Create your views here.

def fun(request):
    res=""
    f1=Fields()
    if request.method =="POST":
        f1=Fields(request.POST)
        if f1.is_valid():
            val1=f1.cleaned_data['num1']
            val2=f1.cleaned_data['num2']
            operator=f1.cleaned_data['operation']
            if operator=='Add':
                res=val1+val2
            if operator == 'Sub':
                res=val1-val2
            if operator == 'Mul':
                res=val1*val2
            if operator == 'Div':
                res=val1/val2
    
    return render(request,'index.html',{'form':f1,'res':res})
