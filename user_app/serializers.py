from rest_framework import serializers
from user_app.models import CustomUser,Customer,Project
import re

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta():
        model = CustomUser
        fields = ['email','password']
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
class SetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    def validate_password(self,value):
        if len(value)<8:
            raise serializers.ValidationError('Password must me 8 characters long')
        if not re.search(r'[A-Z]',value):
            raise serializers.ValidationError('Password must contain at least one upper case letter')
        if not re.search(r'[a-z]',value):
            raise serializers.ValidationError('Password must contain at least one lower case letter')
        if not re.search(r'[@$!%*?&#]',value):
            raise serializers.ValidationError('Password must contain at least one special character')
        return value
    
    def validate(self,data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Passwords do not match')
        return data
        
class ProjectSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.customer_name',read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'master_project_id',
            'child_project_id',
            'project_name',
            'project_type',
            'service_offering',
            'project_status',
            'customer',
            'customer_name',
        ]
        
class CustomerSerializer(serializers.ModelSerializer):
    projects = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'