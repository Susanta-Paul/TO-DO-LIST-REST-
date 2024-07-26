from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todo.models import Task
from todo.serializers import TaskSerializer
from rest_framework import status
from rest_framework import generics

# Create your views here.
def index(request):
  return render(request, "todo/index.html")

@api_view(["GET", "POST"])
def all(request):
  if request.method=="GET":
    items=Task.objects.all()
    item_serial=TaskSerializer(items, many=True)
    return Response(item_serial.data)

  elif request.method=="POST":
    new_serial=TaskSerializer(data=request.data)
    if new_serial.is_valid():
      new_serial.save()
      return Response(new_serial.data, status=status.HTTP_201_CREATED)
    return Response(new_serial.data, status=status.HTTP_400_BAD_REQUEST)



@api_view(["DELETE"])
def delete(request, id):
  try:
    task=Task.objects.get(pk=id)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  # if request.method=="GET":
  #   items=Task.objects.all()
  #   item_serial=TaskSerializer(items, many=True)
  #   return Response(item_serial.data)

  if request.method=="DELETE":
    operation=task.delete()
    data={}
    if operation:
      data["success"]="delete successful"
    else:
      data["fail"]="fails to delete"
    return Response(data=data)

