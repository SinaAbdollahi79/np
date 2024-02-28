from rest_framework import serializers
from django.core import exceptions
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ...models import Profile

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password1']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError({'detail': 'Passwords do not match'})

        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': e.messages})    
   
    
        return super().validate(attrs)
    

    def create(self, validated_data):
        validated_data.pop('password1',None)
        return User.objects.create_user(**validated_data)
    



#rewrite serializer for show email insted usename for token

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    

# custom jwt for show email and id 
class CustomTokenObtainPairSerializer (TokenObtainPairSerializer):

    def validate(self, attrs): 
        validated_data = super().validate(attrs)
        validated_data["email"] = self.user.email
        validated_data["user_id"] = self.user.id

        return validated_data
    

#change profile
class ChangePasswordserializer(serializers.Serializer):
    model = User
    #fields = ['old_password', 'new_password', 'new_password1']

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    #check the new  password is macth with new password 1 
    def validate(self, attrs):
        
        if attrs.get('new_password') != attrs.get('new_password1'):
            raise serializers.ValidationError({'detail': 'Passwords do not match'})

        try:
            validate_password(attrs.get('new_password1'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'new_password': e.messages})
        return super().validate(attrs)
    


class ProfileSerializer(serializers.ModelSerializer):
    email=serializers.CharField(source='User.email',read_only=True)
    class Meta:
        model = Profile
        fields = ('id','email','first_name','last_name','img','description')
        read_only_fields = ['email']





    


