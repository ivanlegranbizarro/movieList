from rest_framework import serializers
from watchlist_app.models import WatchList, StreamingPlatform, Reviews


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reviews
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    len_title = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = '__all__'

    def get_len_title(self, object):
        length = len(object.title)
        return length


class StreamingPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamingPlatform
        fields = '__all__'

    #
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('name and description should be different!')
    #     else:
    #         return data
    #
    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError('Name is too short. Must have at least 3 characters')
    #     else:
    #         return value

    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get(
    #         'description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance

