from django.contrib import admin
from django.urls import path
from db_app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.StudentFormViev.as_view(), name='student_form'),
    path('form/success/', TemplateView.as_view(template_name='feedback.html'), name='success'),
    path('students/table/', views.student_list, name='student_list'),
    path('', views.find_student, name='find_student'),
]
