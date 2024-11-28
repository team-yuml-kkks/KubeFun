import os
from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .models import SensorReadModel


@csrf_exempt
@require_http_methods(["POST"])
def save_sensor_data(request):
    token = request.headers.get('Authorization')
    expected_token = os.getenv('API_TOKEN')
    
    if not token or token != f'Token {expected_token}':
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    SensorReadModel.objects.create(
        timestamp=datetime.now(), value=request.POST['value'],
    )

    return HttpResponse(status=204)
