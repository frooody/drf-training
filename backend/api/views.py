from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    #print(request.header)
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    #print(data)
    return JsonResponse(data)