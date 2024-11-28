from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
import os

from .services import send_notification

@csrf_exempt
@require_http_methods(["POST"])
def notify(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header.split(' ')[1] != os.getenv('API_TOKEN'):
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    try:
        value = request.POST.get('value')
        if not value:
            return JsonResponse({'error': 'Value is required'}, status=400)

        if value > 100:
            send_notification(value)
        
        return JsonResponse({'status': 'notification sent'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
