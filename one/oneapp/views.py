from django.shortcuts import render
from django.shortcuts import HttpResponse
from . models import place
from . models import team

# Create your views here.


def demo(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request, "index.html",{'result':obj,'team':obj1})
    # return render(request, "home.html")
# def teamfn(request):
#     o=team.objects.all()
#     return render(request,"index.html",{'teamof':o})

def operations(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add1=x+y
    mul1=x*y
    sub1=x-y
    div1=x/y
    return render(request,"result.html",{'add1':add1,'mul1':mul1,'sub1':sub1,'div1':div1,'x1':x,'y2':y})
