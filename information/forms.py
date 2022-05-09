from dataclasses import field
from django import forms
from .models import Student


class Studentforms(forms.ModelForm):
    
    
    class Meta:
        model  = Student
        fields= [
             "name","roll_num","email","mobile"
         ]