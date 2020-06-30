# -*- coding: utf-8 -*-
from django import forms
from .models import Details,profile1,blog



class Detailsform(forms.ModelForm):
    class Meta:
        model=Details
        fields=['eid','ename','eemail','econtact','Img']
        
class Profileform(forms.ModelForm):
    class Meta:
        model=profile1
        fields=['name','email','Img']
        
class Blogform(forms.ModelForm):
    class Meta:
        model=blog
        fields=['Img','title','content']