# mysite/serializers.py
from rest_framework import serializers
from .models import AiAnalysisLog

class AiAnalysisLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = AiAnalysisLog
		fields = '__all__'