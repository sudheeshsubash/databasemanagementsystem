from rest_framework.views import APIView,status
from rest_framework.response import Response
from django.apps import apps
from .serializers import ModelSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_table_list(request):
    models = apps.get_app_config('api').get_models()
    data = list()
    for model in models:
        data_list = {}
        data_list[f"{model.__name__}"] = reverse('manipulationview',kwargs={'modelname':model.__name__},request=request)
        data.append(data_list)
    return Response(data)



class DynamicModelDataManipulationView(APIView):
    '''
    Users can select tables dynamically 
    and perform (GET,POST) operations
    
    GET:
        retrive all data from choosed model
    POST:
        Add new object to choosed model
        
    '''
    permission_classes = [IsAuthenticated]
    
    def get(self, request, **kwargs):
        try:
            model =  apps.get_app_config('api').get_model(kwargs.get('modelname'))
            serializer_object=ModelSerializer(instance=model.objects.all(),model=model,many=True)
            return Response(serializer_object.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"{e}",status=status.HTTP_404_NOT_FOUND)


    def post(self, request, **kwargs):
        try:
            model =  apps.get_app_config('api').get_model(kwargs.get("modelname"))
            serializer_object = ModelSerializer(model=model,data=request.data)
            serializer_object.is_valid(raise_exception=True)
            serializer_object.save()
            return Response(serializer_object.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"{e}",status=status.HTTP_404_NOT_FOUND)
        


class DynamicModelDataActionView(APIView):
    '''
    Users can select tables dynamically 
    and perform (GET,PUT,DELET) operations
    
    GET:
        retrive one data object from choosed model
    PUT:
        Edit one data object from choosed model
    DELETE:
        Delete one data object form choosed model
    '''    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, **kwargs):
        try:
            model = apps.get_app_config('api').get_model(kwargs.get('modelname'))
            model_object = model.objects.get(id=kwargs.get('pk'))
            serializer_object = ModelSerializer(instance=model_object,model=model)
            return Response(serializer_object.data)
        except Exception as e:
            return Response(f"{e}",status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    
    def put(self, request, **kwargs):
        try:
            model =  apps.get_app_config('api').get_model(kwargs.get('modelname'))
            model_object = model.objects.get(id=kwargs.get('pk'))
            serializer_object = ModelSerializer(model=model,instance=model_object,data=request.data)
            serializer_object.is_valid(raise_exception=True)
            serializer_object.save()
            return Response(serializer_object.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"{e}",status=status.HTTP_404_NOT_FOUND)

    
    
    def delete(self, request, **kwargs):
        try:
            model =  apps.get_app_config('api').get_model(kwargs.get("modelname"))
            model.objects.get(id=kwargs.get('pk')).delete()
            return Response(f"delete data object from {model.__name__}",status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"{e}",status=status.HTTP_404_NOT_FOUND)
