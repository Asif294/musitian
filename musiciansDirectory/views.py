from django.shortcuts import render
from albumAp.models import Album
def home(request):
    data=Album.objects.all()
    return render(request,'index.html',{'data':data})