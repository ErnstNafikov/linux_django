from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import FraudScore
from .serializer import FraudScoreSerializer
from model_nn import kernel

class GetFraudScore(APIView):
    def post(self,request):
        serializer = FraudScoreSerializer(data=request.data)
        fraudScore = None
        if serializer.is_valid(raise_exception=True):
            fraudScore = serializer.save()
        print(fraudScore.id)
        fraudScore.flg_fraud = kernel.resp(fraudScore)
        fraudScore.save()
        output = {
            "FraudScore": fraudScore.flg_fraud
        }
        return Response(output)
        
class Training(APIView):
    def get(self,request):
        n = request.GET.get('epoch')
        kernel.training(n)
        return HttpResponse('ok')
