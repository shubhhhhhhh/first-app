from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
# @xapi_view(['GET'])
# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }

@api_view(['POST'])
def add_account (request) :
    res = {}
    try :
        accountModel = AccountModel()
        accountSerializer = AccountSerializer(accountModel,data=request.data)
        
        if(accountSerializer.is_valid()):
            accountSerializer.save()
            # print("ok1",accountSerializer.data,accountSerializer)            
            refresh = RefreshToken.for_user(accountModel)
            print("ok2",refresh)            
            res['status'] = "success"
            res['refresh'] = str(refresh)
            res['access'] = str(refresh.access_token)
            res['userData'] = accountSerializer.data
            return Response(res)
        else:
            return Response(accountSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as es:
        print(es)
        res['status'] = 'failed'
        return Response(res)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_account_detail_list(request):
    res = {}
    try:
        all_account = AccountModel.objects.all()
        all_account_s = AccountSerializer(all_account,many=True)
        return Response(all_account_s.data)
    except Exception as e:
        res['status'] = 'failed'
        return Response(res)
    

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_account_detail_list_single(request,id):
    res = {}
    try:
        all_account = AccountModel.objects.get(id=id)
        all_account_s = AccountSerializer(all_account)
        return Response(all_account_s.data)
    except Exception as e:
        res['status'] = 'failed'
        return Response(res)

