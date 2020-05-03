from rest_framework import serializers
from .models import Pasta, CATEGORIES

class PastaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pasta
		fields = ['id','text', 'date_created', 'name', 'category']
