from django.shortcuts import render

# Create your views here.
# core/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Organization, Member, Role
from .serializers import UserSerializer, OrganizationSerializer, MemberSerializer, RoleSerializer

class SignUpView(APIView):
    def post(self, request):
        # Handle sign up logic here
        pass

class SignInView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class ResetPasswordView(APIView):
    def post(self, request):
        # Handle password reset logic here
        pass

class InviteMemberView(APIView):
    def post(self, request):
        # Handle invite member logic here
        pass

class DeleteMemberView(APIView):
    def delete(self, request, pk):
        # Handle delete member logic here
        pass

class UpdateMemberRoleView(APIView):
    def put(self, request, pk):
        # Handle update member role logic here
        pass

class RoleWiseUserStatsView(APIView):
    def get(self, request):
        # Handle role wise user stats logic here
        pass

class OrganizationWiseMemberStatsView(APIView):
    def get(self, request):
        # Handle organization wise member stats logic here
        pass

class OrganizationWiseRoleWiseUserStatsView(APIView):
    def get(self, request):
        # Handle organization wise role wise user stats logic here
        pass
