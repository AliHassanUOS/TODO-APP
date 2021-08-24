from django import forms
from .models import Todo

from django.forms.models import ModelForm



class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ("task","completed",)

        widgets = {
 
            
           'task' : forms.TextInput(attrs={'class':'form-control' }),
           'completed': forms.CheckboxInput(attrs={'class':'form-control'}),
           

        }


        


    

        
