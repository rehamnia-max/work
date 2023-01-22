from rest_framework import serializers
from work_app.models import Worker, Work

class WorkerSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="pk", read_only=True)
    username = serializers.CharField()
    birth_date = serializers.DateField()
    phone = serializers.CharField()
    avatar = serializers.ImageField()
    # work_set = serializers.PrimaryKeyRelatedField(queryset=Work.objects.all())
    work_set = serializers.StringRelatedField(many=True)

    # works_set = serializers.StringRelatedField(many=True)
    # work_set = serializers.PrimaryKeyRelatedField(queryset=Work.objects.all())
    # works = WorkSerializer(
    #     read_only=True, many=True, required=False
    # )

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        print('#'*20)
        for d in validated_data:
            print(d)
        return Worker.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)