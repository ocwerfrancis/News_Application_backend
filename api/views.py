from django.shortcuts import render
from .serializers import WeatherSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .weather import weather

# Create your views here.

class WeatherView(GenericAPIView):
	serializer_class = WeatherSerializer

	def post(self, request):
		city = request.data['city']
		print(f"location => {city}")
		city = city + "weather"
		data = weather(city)
		print(f"data => {data}")
		return Response(data, status.HTTP_201_CREATED)