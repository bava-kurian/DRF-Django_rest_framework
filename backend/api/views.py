from django.http import JsonResponse
import json
from product.models import product
from django.forms.models import model_to_dict
def api_response(request,*args,**kwargs):
    model_data=product.objects.all().orderby('?').first()
    body=request.body
    print(request.GET)
    data={}
    try:
        data=json.loads(body)
    except:
        pass
    data=model_to_dict(model_data)
    
    return JsonResponse(data)