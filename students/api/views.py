from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework import status
from .serializers import StudentSerializer
from students.models import Student

class StudentListManual(APIView):    
    def get(self, request, pk=None):        
        if not pk:
            students = Student.objects.all()
            serializer = StudentSerializer(students,many=True)
            return Response(serializer.data,status =status.HTTP_200_OK)
           
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data,status =status.HTTP_200_OK)



class LCStudent(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)    


# RETREIVE ,UPDATE and DELETE Combine 

class RUDStudent(GenericAPIView, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)  
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)

