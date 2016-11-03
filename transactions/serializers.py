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

class StartedTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Started
        fields = ('nu', 'nu_total', 'nu_compare','dau', 'dau_total', 'dau_compare', 'dated')

class CompletedTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Completed
        fields = ('nu', 'nu_total', 'nu_compare','dau', 'dau_total', 'dau_compare', 'dated')


class CompletedDropTrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompletedDrop
        fields = ('nu', 'nu_total', 'nu_compare','dau', 'dau_total', 'dau_compare', 'dated')

class TrendsSerializer(serializers.Serializer):
	started = StartedTrendSerializer(many=True)
	completed = CompletedTrendSerializer(many=True)
	completed_drop = CompletedDropTrendSerializer(many=True)