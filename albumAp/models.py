from django.db import models
from django import forms
from musicianAp.models import MusicianModel
class Album(models.Model):
    aulbum_name=models.CharField(max_length=35)
    musiciam=models.ForeignKey(MusicianModel,on_delete=models.CASCADE)
    relese_date=models.DateField('Date')
   
    choice=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    Ratting=models.CharField(max_length=10,choices=choice,default='1')


    def __str__(self):
        return self.aulbum_name
    
