from .serializers import bankSerializer, branchSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from . import models


@api_view(['GET'])
@permission_classes((AllowAny,))
def findByIfscCode(request):

    if request.method == 'GET':
         ifsc_code = request.query_params.get('ifsc_code', None)
         if ifsc_code is not None:
            queryset = models.branches.objects.filter(ifsc=ifsc_code)
            serializer = branchSerializer(queryset, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
         else:
             return Response({'error':'No Data Found'},status= HTTP_404_NOT_FOUND)   
			
	
	 

@api_view(['GET'])
@permission_classes((AllowAny,))
def findByBankNameCity(request):

   if request.method == 'GET':
         bank_name = request.query_params.get('bank_name', None)
         city = request.query_params.get('city', None)
         if bank_name is not None and city is not None:
           
            bank = models.banks.objects.values_list('id', flat=True).filter(
                        name=bank_name)
            queryset = models.branches.objects.filter(bank_id__in=[bank], city=city)
            serializer = branchSerializer(queryset, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
         else:
             return Response({'error':'No Data Found'},status= HTTP_404_NOT_FOUND)  
			
