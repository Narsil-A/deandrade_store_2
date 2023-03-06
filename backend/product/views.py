from django.http import JsonResponse
import json 


def api_home(request, *args, **kwargs):
    # request -> httpRequest -> Django
    # print(dir(request))
    # request.body
    print(request.GET)

    body = request.body # byte string of JSON data
    print(body)

    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)


