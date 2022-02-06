
from rest_framework.decorators import api_view
from rest_framework.request import Request
from django.http.request import HttpRequest

from typing import Union
from rest_framework.response import Response
from calc.parser import Parser

@api_view(["GET"])
def handleEquations(request : Union[Request, HttpRequest]):
    
    params = request.query_params
    if 'eq' not in params:
        return Response("equations not found in query params", 404)
    try:
        return Response(Parser(params['eq']).parseEquation().eval(), status=200)
    except Exception as e:
        return Response(str(e), status=200)



from rest_framework.views import APIView
class CoffeeTest(APIView):
    def get(self, request: Union[Request, HttpRequest], coffeeID:str):
        return Response("WOW", status = 501)