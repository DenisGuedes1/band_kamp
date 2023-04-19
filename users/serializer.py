from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="This field must be unique.")]
    )
   
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'first_name', 'last_name', 'is_superuser']
        extra_kwargs = {
            'password':{'write_only': True},
            'id':{'read_only': True},
            'is_superuser':{'read_only': True},
        }


    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data, is_superuser=True)
      
        if password is not None:
            instance.set_password(password)
        instance.save()    
     
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        print(f"esse é o validate: {validated_data}")
        print(f"nova senha1:{password}")
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if password:
            instance.set_password(password)
            print(f"nova senha:{password}")
        instance.save()
        return instance