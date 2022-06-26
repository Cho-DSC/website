from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import lotto
from .serializers import lottoSerializer

# Create your views here.
@api_view(['GET'])
def lottoAPI(request):
    totalLotto = lotto.objects.all()
    serializer = lottoSerializer(totalLotto, many=True)
    return Response(serializer.data)


