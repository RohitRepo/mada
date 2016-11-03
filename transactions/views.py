from datetime import datetime

from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from .models import Started, Completed, CompletedDrop
from .serializers import StartedSerializer, CompletedSerializer, CompletedDropSerializer, All, AllSerializer

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_all(request, day, format=None):
	try:
		day_date = datetime.strptime(day, "%Y-%m-%d").date()

		row_started = Started.objects.get(dated=day_date)
		row_completed = Completed.objects.get(dated=day_date)
		row_completed_drop = CompletedDrop.objects.get(dated=day_date)

		all_model = All(started=row_started, completed=row_completed, completed_drop=row_completed_drop)
		serializer = AllSerializer(all_model)

		return Response(serializer.data)
	except Exception as ex:
		print ex
		return Response()

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def started(request, day, format=None):
	try:
		day_date = datetime.strptime(day, "%Y-%m-%d").date()
		row = Started.objects.get(dated=day_date)
		serializer = StartedSerializer(row)
		return Response(serializer.data)
	except Exception as ex:
		print ex
		return Response()

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def completed(request, day, format=None):
	try:
		day_date = datetime.strptime(day, "%Y-%m-%d").date()
		row = Completed.objects.get(dated=day_date)
		serializer = CompletedSerializer(row)
		return Response(serializer.data)
	except Exception as ex:
		print ex
		return Response()

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def completed_drop(request, day, format=None):
	try:
		day_date = datetime.strptime(day, "%Y-%m-%d").date()
		row = CompletedDrop.objects.get(dated=day_date)
		serializer = CompletedDropSerializer(row)
		return Response(serializer.data)
	except Exception as ex:
		print ex
		return Response()