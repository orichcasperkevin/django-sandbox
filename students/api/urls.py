from django.urls import path
from students.api import views

urlpatterns = [
    path('get-students/',views.StudentListManual.as_view()),
    path('get-student/<int:pk>/',views.StudentListManual.as_view())
]