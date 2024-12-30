from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100,required=True)
    last_name = serializers.CharField(max_lenght=100, required= True)
    address = serializers.CharField(max_length=100, required= True)
    roll_number = serializers.IntegerField()
    mobile = serializers.IntegerField(max_length=100, required = True)

    class Meta:
        model= Students
        fields = ('__all__')