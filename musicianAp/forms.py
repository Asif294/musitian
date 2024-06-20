from django.db import models
from django.forms import ModelForm
from . models import MusicianModel
class MusicianForm(ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'