from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta :
        model = AccountModel
        # fields = ["name","email","password"]
        fields = "__all__"