from django.shortcuts import render, redirect
from .forms import StudentForm, StudentFormID
from .models import Student
from django.views.generic import View
# Create your views here.

# Student Form View #
class StudentFormViev(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'forms.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('success')

        return render(request, 'forms.html', {'form': form})  
      
    
# Show all students table #
def student_list(request):
    students = Student.objects.all()
    return render(request, 'table.html', {'students': students})


# Find student by ID #
def find_student(request):
    form = StudentFormID(request.POST or None)
    student = None
    error = None

    if request.method == "POST" and form.is_valid():
        student_id = form.cleaned_data['id']
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            error = "Student with this ID does not exist."

    return render(request, 'index.html', {'form': form, 'student': student, 'error': error})

       