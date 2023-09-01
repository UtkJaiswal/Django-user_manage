from rest_framework import generics, permissions, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            return Response({'detail': 'Invalid credentials'}, status=401)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({'access_token': access_token, 'refresh_token': refresh_token})

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            if user.id:
            # authorization_header = request.META.get('HTTP_AUTHORIZATION', '')
            # print("Auth",authorization_header)

            # Check if the header starts with 'Bearer'
            # if authorization_header.startswith('Bearer '):
                # Extract the token part (after 'Bearer ')
                # token = authorization_header.split(' ')[1]

                # Try to find the AccessToken based on the token
                # access_token = AccessToken.objects.get(token=token)

                # Blacklist the AccessToken
                # access_token.blacklist()
            # if hasattr(user, 'auth_token'):
            #     access_token = AccessToken(user.auth_token.key)
            #     access_token.blacklist()

                refresh_token = RefreshToken(request.data['refresh_token'])
                refresh_token.blacklist()

                return Response({'detail': 'Successfully logged out.'})
            return Response({"message":"Unauthorized user"},status=401)

        except Exception as e:
            return Response({'error': 'Token is invalid or expired','message':str(e)}, status=400)
        

    
class UserDetailsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

