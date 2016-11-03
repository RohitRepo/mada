from rest_framework import serializers
from .models import Opens, Rejects, OpensSocial, RejectsSocial, OpensCommerce, RejectsCommerce

class OpensSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opens

class RejectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rejects

class OpensSocialSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpensSocial

class RejectsSocialSerializer(serializers.ModelSerializer):

    class Meta:
        model = RejectsSocial

class OpensCommerceSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpensCommerce

class RejectsCommerceSerializer(serializers.ModelSerializer):

    class Meta:
        model = RejectsCommerce

class All(object):
	"""docstring for All"""
	def __init__(self, opens, rejects, opens_social, rejects_social, opens_commerce, rejects_commerce):
		super(All, self).__init__()
		self.opens = opens
		self.rejects = rejects
		self.opens_social = opens_social
		self.rejects_social = rejects_social
		self.opens_commerce = opens_commerce
		self.rejects_commerce = rejects_commerce
		
class AllSerializer(serializers.Serializer):
	opens = OpensSerializer()
	rejects = RejectsSerializer()
	opens_social = OpensSocialSerializer()
	rejects_social = RejectsSocialSerializer()
	opens_commerce = OpensCommerceSerializer()
	rejects_commerce = RejectsCommerceSerializer()
