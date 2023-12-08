from django.shortcuts import render
from .models import Quote
# Create your views here.


def home(request):
    content=Quote.objects.all()
    return render(request,'quote/home.html',{'content':content})



def searchID(request):
    if request.method=='GET':
        q=request.GET.get('q')
        if q:
            content=Quote.objects.filter(auther__icontains=q)
            return render(request,'quote/search.html',{'content':content})
        else:
            print('NO information to show')
            return render(request,'quote/search.html')


