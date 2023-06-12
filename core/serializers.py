from rest_framework import serializers
from core.models import Item

class PostSerializers(serializers.ModelSerializer):

    class Meta:

        model = Item

        exclude = ['is_removed', 'created', 'modified']