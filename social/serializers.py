from rest_framework import serializers
from .models import Likes, Comments, Shares, ProfileViews

class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes

class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments

class SharesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shares

class ProfileViewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileViews

class All(object):
	"""docstring for All"""
	def __init__(self, likes, comments, shares, profile_views):
		super(All, self).__init__()
		self.likes = likes
		self.comments = comments
		self.shares = shares
		self.profile_views = profile_views
		
class AllSerializer(serializers.Serializer):
	likes = LikesSerializer()
	comments = CommentsSerializer()
	shares = SharesSerializer()
	profile_views = ProfileViewsSerializer()