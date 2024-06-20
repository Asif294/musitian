from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.add_musician,name='musician'),
   path('edit_mu/<int:id>',views.edit_musician,name='edit_musician')
]
