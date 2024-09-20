from django.http import JsonResponse
import json
def api_response(request,*args,**kwargs):
    body=request.body
    print(request.GET)
    data={}
    try:
        data=json.loads(body)
    except:
        pass
    data["content-type"]=request.content_type
    return JsonResponse(data)