import os
import random
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(["GET"])
def sensors_data(request):
    token = request.headers.get('Authorization')
    expected_token = os.getenv('API_TOKEN')
    
    if not token or token != f'Token {expected_token}':
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    value = random.randint(0, 40000)
    return JsonResponse({'value': value})
