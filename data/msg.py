from pydantic import BaseModel
from enum import Enum
from django.http import JsonResponse

class Error(Enum):
    GENERAL=['General Error',404]
    LOGIN=['Login Error', 500]


class Msg(BaseModel):
    data:BaseModel=None
    message:str=""

    def msg(data):
        print(Msg(data=data).dict())
        return JsonResponse(Msg(data=data).dict())
    
    def error(error):
        print(error.value[0])
        print(Msg(message=error.value[0]).dict())
        return JsonResponse(Msg(message=error.value[0]).dict(),status=error.value[1])

class TestMsg(BaseModel):
    test:str='111'
    t:str='222'
