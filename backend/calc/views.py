from os import stat
from rest_framework.decorators import api_view
from rest_framework.request import Request
from django.http.request import HttpRequest
import rest_framework.status as status
from typing import Union
from rest_framework.response import Response


@api_view(["GET"])
def handleEquations(request : Union[Request, HttpRequest]):
    
    params = request.query_params
    if 'eq' not in params:
        return Response("equations not found in query params", 404)
    
    return Response("not implemented!!!", status=status.HTTP_501_NOT_IMPLEMENTED)



from rest_framework.views import APIView
class CoffeeTest(APIView):
    def get(self, request: Union[Request, HttpRequest], coffeeID:str):
        return Response("WOW", status = 501)