from datetime import datetime
from itertools import count
from tkinter import W
from django.shortcuts import render
from rest_framework.decorators import APIView

from main.serializer import AdverSerializer, CategorySerializer, PaymentSerializer, WishlistSerializer
from .models import*
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes


class CategoryView(APIView):
    def get(self, request):
        a = Category.objects.all()
        ser = CategorySerializer(a, many=True)
        return Response(ser.data)

class CategoryFilter(APIView):
    def get(self, request):
        category_id = request.GET['id']
        a = Adver.objects.filter(category__id=category_id)
        ser = AdverSerializer(a, many=True)
        n = a.count()

        data = ser.data
        data.insert(0, {'count': n})
        print(n)

        return Response(data)

class UserDetailView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request):
        user = request.user
        a = Adver.objects.filter(user=user)
        ser = AdverSerializer(a, many=True)

        return Response(ser.data) 

    def post(self, request):
        user = request.user
        money = request.POST.get('money')
        date = datetime.now()
        u = User.objects.get(username=user)
        a = Payment.objects.create(user=user, money=money, date=date)
        ser = PaymentSerializer(a, many = True)
        u.debt += int(a.money)
        u.save()
        print(user)
        return Response(ser.data, status=status.HTTP_201_CREATED)

class WishlistView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def post(self, request):
        user = request.user
        adver = request.POST.get('id')
        a = Adver.objects.get(id=adver)
        u = User.objects.get(username=user)
        a = Wishlist.objects.create(user=user, adver=a)
        ser = WishlistSerializer(a)

        return Response(ser.data)

    def get(self, request):
        user = request.user
        a = Wishlist.objects.filter(user_username=user)
        ser = WishlistSerializer(a)

        return Response(ser.data)