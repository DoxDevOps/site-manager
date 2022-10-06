from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Site
from .serializers import SiteSerializer

class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

     # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        sites = Site.objects.filter(user = request.user.id)
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


        # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given site data
        '''
        data = {
            'name': request.data.get('name'), 
            'ip_address': request.data.get('ip_address'), 
            'username': request.data.get('username'),
            'password': request.data.get('password')
        }
        serializer = SiteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
