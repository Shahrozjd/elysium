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
    return render(request, 'index.html')

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

    @action(methods=['post'], detail=False)
    def signup(self, request):
        full_name=request.data.get('full_name', '')
        company_name=request.data.get('company_name', '')
        country=request.data.get('country', '')
        street_address=request.data.get('street_address', '')
        password=request.data.get('password', '')
        city=request.data.get('city', '')
        state=request.data.get('state', '')
        post_code=request.data.get('post_code', '')
        phone=request.data.get('phone', '')
        email=request.data.get('email', '')
        occupation=request.data.get('occupation', '')
        gender=request.data.get('gender', '')
        father_name=request.data.get('father_name', '')
        blood_group=request.data.get('blood_group', '')
        birth_date=request.data.get('birth_date', '')
        religion=request.data.get('religion', '')
        nationality=request.data.get('nationality', '')
        hobby=request.data.get('hobby', '')
        purpose=request.data.get('purpose', '')
        membership_id=request.data.get('membership', '')
        image=request.data.get('image', '')
        try:
            membership = Membership.objects.get(id=membership_id)
            Profile.objects.create(
                full_name=full_name,
                company_name=company_name,
                country=country,
                street_address=street_address,
                password=password,
                city=city,
                state=state,
                post_code=post_code,
                phone=phone,
                email=email,
                occupation=occupation,
                gender=gender,
                father_name=father_name,
                blood_group=blood_group,
                birth_date=birth_date,
                religion=religion,
                nationality=nationality,
                hobby=hobby,
                purpose=purpose,
                image=image,
                membership=membership,
            )
            return Response(data={"res":"Member added successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data={ "res": str(e) }, status=status.HTTP_404_NOT_FOUND)


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class InoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    @action(methods=['post'], detail=False)
    def add(self, request):
        try:
            user_id=request.GET.get('user', '')
            member = Profile.objects.get(id=user_id)
            Attendance.objects.create(member=member)
            return Response(data={"res":"Attendance added successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data={ "res": str(e) }, status=status.HTTP_404_NOT_FOUND)


def invoice_print(request):
    id = request.GET.get('id','')
    invoice = Invoice.objects.get(id=id)
    context={
        'invoice': invoice,
    }
    return render(request, 'print.html', context=context)