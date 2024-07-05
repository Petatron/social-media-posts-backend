from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    bio = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    avatar = serializers.ImageField(allow_null=True, required=False)
