from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate,get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from UserManagement.serializers import UserSerializer
User=get_user_model()
class user_register(APIView):
    def post(self,request):
        serializer_item = UserSerializer(data=request.data)
        serializer_item.is_valid(raise_exception=True)
        user=serializer_item.save()
        refresh = RefreshToken.for_user(user)
        r= {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(r, status=status.HTTP_200_OK)

class user_login(APIView):
    def post(self,request):
        try:
            user = authenticate(**request.data)
            if user:
                refresh = RefreshToken.for_user(user)
                r = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(r, status=status.HTTP_200_OK)
            else:
                return Response("Invalid Credentials", status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            raise e

@permission_classes(([IsAuthenticated]))
class user_password_change(APIView):
    def patch(self,request):
        user = User.objects.get(username=request.user)
        if len(request.data) == 1 and "password" in request.data:
            serializer_item = UserSerializer(user, data=request.data, partial=True)
            serializer_item.is_valid(raise_exception=True)
            serializer_item.save()
            return Response("Password Changed",status=status.HTTP_200_OK)
        else:
            return Response("Incorrect Fields",status=status.HTTP_401_UNAUTHORIZED)


@permission_classes(([IsAuthenticated]))
class delete_user(APIView):
    def delete(self,request):
        try:
            user = User.objects.get(username=request.user)
            user.delete()
            return Response("User Deleted",status=status.HTTP_200_OK)
        except Exception as e:
            raise e



