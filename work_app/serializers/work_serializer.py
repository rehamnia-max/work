from rest_framework import serializers
from work_app.models import Work, Worker, Category


class WorkSerializer(serializers.Serializer):

    id = serializers.IntegerField(source="pk", read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    image = serializers.ImageField()
    # worker = serializers.StringRelatedField(many=True)
    worker = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # work = serializers.StringRelatedField(many=False)
    # worker = serializers.DateField()
    # category = serializers.


    def validate(self, attrs):

        return super().validate(attrs)

    def create(self, validated_data):
        print('#'*20)
        # print(**validated_data)
        return Work.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)