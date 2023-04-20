from rest_framework import serializers

from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
     class Meta:
           model = Album
           fields = ['id', 'name', 'year', 'user_id']
    #        fields = ['id', 'name', 'year', 'user_id']
    #        extra_kwargs = {
    #            'user_id':{'read_only':True},
    #     'id':{'read_only':True}
    #        }
    # user_id = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
   
