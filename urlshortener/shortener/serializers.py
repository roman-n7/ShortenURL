from rest_framework import serializers
from .models import URL
from .utils import generate_short_code

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['original_url', 'short_url']
        read_only_fields = ['short_url']

    def create(self, validated_data):
        validated_data['short_url'] = generate_short_code()
        return super().create(validated_data)
    
        
    