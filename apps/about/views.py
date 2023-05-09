from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



from .models import *
from .serializers import *


# Create your views here.
class TeamApi(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.user.is_admin:
            data = request.data
            serializer = TeamSerializer(data= data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status' : 'True','body': serializer.data}, status.HTTP_200_OK)
            else:
                return Response({'status' : 'False','body': serializer.errors}, status.HTTP_400_BAD_REQUEST)
        else: 
            return Response({'status' : 'False','message': 'Unauthorized Access Prohibited'}, status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request):
        if request.user.is_admin:
            data = request.data
            obj=Team.objects.get(id = data['id'])
            obj.delete()
            return Response({'status' : 'True','message': 'Member Deleted'}, status.HTTP_200_OK)
        else: 
            return Response({'status' : 'False','message': 'Invalid Access'}, status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])   
def get_team(request):
        Convenor = Team.objects.filter(post_assign="CC").all()
        Manager = Team.objects.filter(post_assign="MM").all()
        Executive = Team.objects.filter(post_assign="EXC").all()

        serializer1 = TeamSerializer(Convenor, many=True)
        serializer2 = TeamSerializer(Manager, many=True)
        serializer3 = TeamSerializer(Executive, many=True)

        dict = {'Convenor': serializer1.data,
                'Manager': serializer2.data, 'Executive': serializer3.data}

        return Response({'status' : 'True','body': dict}, status.HTTP_200_OK)


class Alumini(APIView):

    def get(self, request):
        Alumini = Team.objects.filter(post_assign="AA").all()
        serializer1 = TeamSerializer(Alumini, many=True)
        return Response(serializer1.data)
