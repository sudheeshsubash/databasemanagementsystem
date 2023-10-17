from rest_framework import serializers
from rest_framework.reverse import reverse
from django.urls import get_script_prefix



class ModelSerializer(serializers.ModelSerializer):
    
    def __init__(self, *args, **kwargs):
        self.Meta.model = kwargs.pop('model')
        super().__init__(*args, **kwargs)
    
    url = serializers.SerializerMethodField()
    
    def get_url(self, obj):
        request = self.context.get('request')
        relative_url = reverse('actionview',kwargs={"modelname":self.Meta.model.__name__,'pk':obj.pk},request=request)
        return f"http://127.0.0.1:8000{relative_url}"
        
    class Meta:
        fields = '__all__'
