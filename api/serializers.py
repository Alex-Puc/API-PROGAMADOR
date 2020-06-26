from .models import Programmer
from rest_framework import serializers

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ('nick', 'email', 'first_name', 'last_name', 'program_lang')

    