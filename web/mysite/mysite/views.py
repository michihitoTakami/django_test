# mysite/views.py
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import AiAnalysisLog
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AiAnalysisLog
from .serializers import AiAnalysisLogSerializer
from datetime import datetime
from django.utils import timezone

@csrf_exempt
def ai_analysis(request):
	if request.method == 'POST':
		try:
			data = json.loads(request.body)
		except json.JSONDecodeError:
			return JsonResponse({'error': 'Invalid JSON'}, status=400)

		image_path = data.get('image_path')

		if not image_path:
			return JsonResponse({'error': 'image_path is required'}, status=400)

		request_timestamp = timezone.now()

		response = requests.post('http://mock_server:5000', json={'image_path': image_path})
		response_data = response.json()
		response_timestamp = timezone.now()

		log = AiAnalysisLog(
			image_path=image_path,
			success=response_data.get('success'),
			message=response_data.get('message'),
			class_field=response_data.get('estimated_data', {}).get('class'),
			confidence=response_data.get('estimated_data', {}).get('confidence'),
			request_timestamp=request_timestamp,
			response_timestamp=response_timestamp
		)
		log.save()

		if response_data.get('success'):
			return JsonResponse(response_data, status=200)
		else:
			return JsonResponse(response_data, status=500)
	else:
		return JsonResponse({'error': 'Invalid request method'}, status=405)
	
class AiAnalysisLogView(APIView):
    def get(self, request, *args, **kwargs):
        date_str = request.query_params.get('date')
        if date_str:
            try:
                date = datetime.strptime(date_str, '%Y%m%d').date()
            except ValueError:
                return Response({"error": "Invalid date format. Use YYYYMMDD."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            date = timezone.now().date()

        logs = AiAnalysisLog.objects.filter(request_timestamp__date=date)
        serializer = AiAnalysisLogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)