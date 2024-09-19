from django.http import JsonResponse
import json
def api_response(request,*args,**kwargs):
    body=request.body
    print(request.body)
    data={}
    try:
        data=json.loads(body)
    except:
        pass
    return JsonResponse({"MEssage":"This is api"})