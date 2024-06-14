from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _


User = get_user_model()

class loginSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("email"))
    password = serializers.CharField(
        label = _("password"),
        style = {'input type': 'password'},
        trim_whitespace = False,
        write_only = True
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email and password:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        else:
            return data

class signupSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = '__all__'

    def validate_email(self, data):
        if User.objects.filter(email=data).exists():
            raise serializers.ValidationError("A user with this email already exists")
        return data
