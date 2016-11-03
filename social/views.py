from datetime import datetime

from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from .models import Likes, Comments, Shares, ProfileViews
from .serializers import All, AllSerializer

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_all(request, day, format=None):
	try:
		day_date = datetime.strptime(day, "%Y-%m-%d").date()

		row_likes = Likes.objects.get(dated=day_date)
		row_comments = Comments.objects.get(dated=day_date)
		row_shares = Shares.objects.get(dated=day_date)
		row_profile_views = ProfileViews.objects.get(dated=day_date)

		all_model = All(likes=row_likes, comments=row_comments,shares=row_shares, profile_views=row_profile_views)
		serializer = AllSerializer(all_model)

		return Response(serializer.data)
	except Exception as ex:
		print ex
		return Response()

