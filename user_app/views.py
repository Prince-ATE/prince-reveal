from rest_framework import status,viewsets,filters,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from user_app.models import CustomUser,Customer,Project
from user_app.serializers import LoginSerializer, SetPasswordSerializer,CustomerSerializer,ProjectSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.first_login:
            return Response({'message': 'Please set your password first'}, status=status.HTTP_200_OK)
        
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login Successful. Redirecting to dashboard.',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def set_password_view(request):
    serializer = SetPasswordSerializer(data=request.data)
    
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.first_login:
            user.set_password(password)
            user.first_login = False
            user.save()
            return Response({'message': 'Password set successfully. You can now log in'}, status=status.HTTP_200_OK)
        
        return Response({'message': 'Password already set. Please log in'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['customer_name',]
    search_fields = ['customer_name','contact_first_name','contact_last_name',]
    ordering_fields = ['customer_id','customer_name','contract_start_date','contract_end_date',]
    ordering = ['customer_id',]
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.select_related('customer').all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['project_type','service_offering','project_status','customer',]
    search_fields = ['project_name','child_project_id']
    ordering_fields = ['master_project_id','child_project_id','project_name','project_type','service_offering','project_status']
    ordering = ['master_project_id',]
    
    