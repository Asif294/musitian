from django.shortcuts import render,redirect
from . import forms
from . models import MusicianModel
def add_musician(request):
    if request.method=="POST":
        MusicianForm=forms.MusicianForm(request.POST)
        if MusicianForm.is_valid():
            MusicianForm.save()
            return redirect("homepage")
    else:
        MusicianForm=forms.MusicianForm()
    return render(request,'musician.html',{'form':MusicianForm})

def edit_musician(request,id):
    music=MusicianModel.objects.get(pk=id) 
    MusicianForm=forms.MusicianForm(instance=music)
    if request.method=='POST':
        MusicianForm=forms.MusicianForm(request.POST, instance=music)
        if MusicianForm.is_valid():
            MusicianForm.save()
            return redirect("homepage")
    return render(request,'musician.html',{'form':MusicianForm})