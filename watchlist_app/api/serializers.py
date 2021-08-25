from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('name and description should be different!')
        else:
            return data

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Name is too short. Must have at least 3 characters')
        else:
            return value

    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get(
    #         'description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance
