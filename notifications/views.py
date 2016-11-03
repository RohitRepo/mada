from datetime import datetime

from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from .models import Opens, Rejects, OpensSocial, RejectsSocial, OpensCommerce, RejectsCommerce
from .serializers import All, AllSerializer

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_all(request, day, format=None):
	try:
		day_date = datetime.strptime(day, "%Y-%m-%d").date()

		row_opens = Opens.objects.get(dated=day_date)
		row_rejects = Rejects.objects.get(dated=day_date)
		row_opens_social = OpensSocial.objects.get(dated=day_date)
		row_rejects_social = RejectsSocial.objects.get(dated=day_date)
		row_opens_commerce = OpensCommerce.objects.get(dated=day_date)
		row_rejects_commerce = RejectsCommerce.objects.get(dated=day_date)

		all_model = All(opens=row_opens,
			rejects=row_rejects,
			opens_social=row_opens_social,
			rejects_social=row_rejects_social,
			opens_commerce=row_opens_commerce,
			rejects_commerce=row_rejects_commerce
		)
		serializer = AllSerializer(all_model)

		return Response(serializer.data)
	except Exception as ex:
		print ex
		return Response()

