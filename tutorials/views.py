from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from googletrans import Translator


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request,):
    if request.method == 'POST':
        form=request.POST.get('amount')
        translator = Translator()
        result= translator.translate(f'{form}',dest="fr").text
        print(result)
        
        return JsonResponse(result, safe=False)


 