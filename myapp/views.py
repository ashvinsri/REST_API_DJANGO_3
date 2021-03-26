from django.shortcuts import render
# from rest_framework.parsers import JSONParser
from myapp.serializers import StudentSerializers
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# import io
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myapp.models import Student

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method=='GET':
        clas=request.data.get('clas')
        if clas is not None:
            stu=Student.objects.get(clas=clas)
            serializer=StudentSerializers(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializers(stu,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created!!'})
        return Response(serializer.errors)
    if request.method=='PUT':
        clas=request.data.get('clas')
        stu=Student.objects.get(clas=clas)
        serializer=StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializers.errors)
    if request.method=='DELETE':
        clas=request.data.get('clas')
        stu=Student.objects.get(clas=clas)
        stu.delete()
        return Response({'msg':'Deleted'})





# @csrf_exempt
# def student_create(request):
#     if request.method=='POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         serializer=StudentSerializers(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Created'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='Application/json')
#         json_data=JSONRenderer().render(serializer.error)
#         return HttpResponse(json_data,content_type='Application/json')

# @csrf_exempt
# def student_update(request):
#     if request.method=='GET':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         ids=python_data.get('id',None)
#         if ids is not None:
#             stu=Student.objects.get(clas=ids)
#             serializer=StudentSerializers(stu)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='Application/json')
#         stu=Student.objects.all()
#         serializer=StudentSerializers(stu,many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='Application/json')
    
#     if request.method=='POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         serializer=StudentSerializers(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'created'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
    
#     if request.method=='PUT':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         ids=python_data.get('clas')
#         stu=Student.objects.get(clas=ids)
#         serializer=StudentSerializers(stu,data=python_data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data Updated!!!'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
    
#     if request.method=='DELETE':
#        json_data=request.body
#        stream=io.BytesIO(json_data)
#        python_data=JSONParser().parse(stream)
#        ids=python_data.get('clas')
#        stu=Student.objects.get(clas=ids)
#        stu.delete()
#        res={'msg':'Data Deleted!!'}
#        json_data=JSONRenderer().render(res)
#        return HttpResponse(json_data,content_type='application/json')
    
    
       
 




