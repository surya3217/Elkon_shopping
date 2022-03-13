from django.shortcuts import redirect,render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Max

@api_view(['GET'])
def home(request):
    context = {'message':'Welcome in Flamingo project'}
    print(context)
    return Response(context)


@api_view(['GET'])
def insert(request):
    try:
        time = request.query_params.get("timestamp")
        value = request.query_params.get("value")
        print(time, value)
        if request.method == "GET":
            entry = Value.objects.filter(timestamp= time, value= value).first()
            if entry:
                return Response({'message':'data already exist'})
            else:
                obj= Value.objects.create(
                    value= value,
                    timestamp= time
                )
                obj.save()
                return Response({'message':'added successfully'})
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def graph(request):
    try:
        if request.method == "GET":
            all_data= Value.objects.values('timestamp').annotate(value= Max('value')).order_by('timestamp')
            serializer = ValueSerializer(all_data, many=True)
            return Response({'data': serializer.data})
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)

