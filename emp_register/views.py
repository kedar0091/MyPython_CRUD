from django.shortcuts import render
from .models import Employee
# Create your views here.
from .serializers import SnippetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

      

@api_view(['POST'])
def add_data(request):
    try:
        fname = request.data['fname']
        lname = request.data['lname']
        email = request.data['email']
        Employee.objects.create(fname=fname, lname=lname, email=email)
        return Response(data="Success")
    except:
        return Response(data="Json key error")



@api_view(['POST'])
def login(request):
    try:
        id = request.data['id']
        email = request.data['email']
        emp = Employee.objects.get(email=email,id=id)
        return Response(data='success')
    
    except:
          return Response(data="User Not Found!!")




@api_view(['GET'])
def get_data(request):
        try:
            id = request.data['id']
            emp = Employee.objects.get(id=id)
            return Response(data={emp.fname, emp.lname, emp.email})
        except:
            return Response(data="data not found")


@api_view(['GET'])
def getall_data(request):
    try:
        emp = Employee.objects.all()
        serializer = SnippetSerializer(emp, many=True)
        return Response(serializer.data)
    except:
        return Response(data="insert proper data")



@api_view(['PUT'])
def update_data(request):
    try:
        id = request.data['id']
        fname = request.data['fname']
        lname = request.data['lname']
        email = request.data['email']

        emp = Employee.objects.get(id=id)
        emp.fname = fname
        emp.lname = lname
        emp.email = email
        emp.save()
        return Response(data="success")
    except:
        return Response(data="data not found")


@api_view(['DELETE'])
def delete_data(request):
    try:
        id = request.data['id']
        emp = Employee.objects.get(id=id)
        emp.delete()
        return Response(data="Success")

    except:
        return Response(data="Data Not Found")