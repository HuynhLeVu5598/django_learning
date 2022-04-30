from .models import Course
from django import forms

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','price','content','image','slug']
    
