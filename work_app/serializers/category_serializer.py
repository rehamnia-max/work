from rest_framework import serializers
from work_app.models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(source="pk", read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
