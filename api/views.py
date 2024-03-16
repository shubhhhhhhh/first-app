from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def add_account (request) :
    res = {}
    try :
        accountModel = AccountModel()
        accountSerializer = AccountSerializer(accountModel,data=request.data)
        if(accountSerializer.is_valid()):
            accountSerializer.save()
            return Response(accountSerializer.data)
        else:
            Response(accountSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as es:
        print(es)
        res['status'] = 'failed'
        return Response(res)