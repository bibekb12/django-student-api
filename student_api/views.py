from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Students
from .serializers import StudentSerializer

class StudentView(APIView):
    # def get(self,request, *args, **kwargs):
    #     result = Students.objects.all()
    #     serial = StudentSerializer(result, many= True)
    #     return Response({"status":"success","students":serial.data},status = status.HTTP_200_OK)
    
    def get(self,request,id=None):
        
        if id:
            result = Students.objects.get(id=id)
            serial = StudentSerializer(result)
            return Response({'success':"success","students":serial.data}, status= 200)
        
        result = Students.objects.all()
        serial = StudentSerializer(result, many= True)
        return Response({"status":"suceess","students":serial.data}, status=200)
    
    def post(self,request):
        serial=StudentSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({"status":"success","data":serial.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serial.errors},status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,id):
        result=Students.objects.get(id=id)
        serial=StudentSerializer(result,data=request.data,partial=True)
        if serial.is_valid():
            serial.save()
            return Response({"status":"success","data":serial.data})
        else:
            return Response({"status":"error","data":serial.errors})
        
    def delete(self,request,id=None):
        result=get_object_or_404(Students,id=id)
        result.delete()
        return Response({"status":"succeded","data":"Record flew !"})