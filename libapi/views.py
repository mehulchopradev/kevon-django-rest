from django.shortcuts import render
from libapi.serializers import PublicationhouseSerializer
from libapi.models import Publicationhouse
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

# Create your views here.

class PublicationView(ListCreateAPIView):
    serializer_class = PublicationhouseSerializer
    # queryset = Publicationhouse.objects.order_by('-ratings')

    def get_queryset(self):
        ratings = self.request.query_params.get('ratings')
        if ratings:
            return Publicationhouse.objects.filter(ratings=ratings)
        return Publicationhouse.objects.order_by('-ratings')

class PublicationRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PublicationhouseSerializer
    queryset = Publicationhouse.objects.all()

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
        if user:
            return Response({"success": True})
        return Response({"success": False}, status=HTTP_401_UNAUTHORIZED)