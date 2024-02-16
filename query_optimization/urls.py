from django.urls import path
from query_optimization.views import test_view

urlpatterns = [
    path('test/', test_view,),    
]