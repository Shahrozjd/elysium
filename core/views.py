from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, viewsets
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse('Hello')

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(methods=['post'], detail=False)
    def login(self, request):
        email=request.GET.get('email', '')
        password=request.GET.get('password', '')
        profile = Profile.objects.filter(email=email, password=password)
        if profile.exists():
            serializer = ProfileSerializer(profile.first())
            return JsonResponse(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    @action(methods=['post'], detail=False)
    def add(self, request):
        user_id=request.GET.get('user', '')
        member = Profile.objects.get(id=user_id)
        Attendance.objects.create(member=member)
        return Response(status=status.HTTP_200_OK)
