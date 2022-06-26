from rest_framework import serializers
from .models import lotto

class lottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = lotto
        fields = ('drwNo', 'drwNoDate', 'drwtNo1', 'drwtNo2', 'drwtNo3', 'drwtNo4', 'drwtNo5', 'drwtNo6', 'dnusNo', 'firstAccumamnt')
        # fields = '__all__'