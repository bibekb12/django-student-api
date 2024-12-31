from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import Students
from .serializers import StudentSerializer

class StudentView(APIView):
    pagination_class = PageNumberPagination
    # def get(self,request, *args, **kwargs):
    #     result = Students.objects.all()
    #     serial = StudentSerializer(result, many= True)
    #     return Response({"status":"success","students":serial.data},status = status.HTTP_200_OK)
    
    def get(self,request,id=None):
        if id:
            result = Students.objects.get(id=id)
            serial = StudentSerializer(result)
            return Response({'success':"success","students":serial.data}, status=status.HTTP_200_OK)
        
        result = Students.objects.all()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(result, request)
        if page is not None:
            serializer = StudentSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = StudentSerializer(result, many=True)
        return Response(serializer.data)

    
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