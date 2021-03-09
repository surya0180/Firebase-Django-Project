from django import forms 
from .models import Stu
  
class FormsHash(forms.ModelForm): 
  
    class Meta: 
        model = Stu 
        fields=["image"]