from rest_framework import serializers
from .models import Started, Completed, CompletedDrop

class StartedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Started

class CompletedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Completed


class CompletedDropSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompletedDrop

class All(object):
	"""docstring for All"""
	def __init__(self, started, completed, completed_drop):
		super(All, self).__init__()
		self.started = started
		self.completed = completed
		self.completed_drop = completed_drop
		
class AllSerializer(serializers.Serializer):
	started = StartedSerializer()
	completed = CompletedSerializer()
	completed_drop = CompletedDropSerializer()