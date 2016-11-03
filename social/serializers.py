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

class LikesTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = ('nu', 'nu_total', 'nu_compare','dau', 'dau_total', 'dau_compare', 'dated')

class CommentsTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ('nu', 'nu_total', 'nu_compare','dau', 'dau_total', 'dau_compare', 'dated')        

class SharesTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shares
        fields = ('nu', 'nu_total', 'nu_compare','dau', 'dau_total', 'dau_compare', 'dated')

class ProfileViewsTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileViews
        fields = ('nu', 'nu_total', 'nu_compare','dau', 'dau_total', 'dau_compare', 'dated')
		
class TrendsSerializer(serializers.Serializer):
	likes = LikesTrendSerializer(many=True)
	comments = CommentsTrendSerializer(many=True)
	shares = SharesTrendSerializer(many=True)
	profile_views = ProfileViewsTrendSerializer(many=True)