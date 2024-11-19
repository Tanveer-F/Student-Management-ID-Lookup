from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class StudentFormID(forms.Form):
    id = forms.IntegerField(label="Student ID", required=True)       