from rest_framework import generics, permissions, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            return Response({'detail': 'Invalid credentials'}, status=401)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token})

class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response({'error': 'Token is invalid or expired'}, status=400)

        return Response({'detail': 'Successfully logged out.'})
    
class UserDetailsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

