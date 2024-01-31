from rest_framework import serializers

# from watchlist_app.api.validators import name_length
from watchlist_app.models import (WatchList, StreamPlatform, Review)


# from watchlist_app.models import Movie


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True) # take 'watchlist' from related_name
    # watchlist = serializers.StringRelatedField(many=True) #if we want to show only what is in __str__
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='watch-details', #take it from urls.py
    )

    class Meta:
        model = StreamPlatform
        fields = "__all__"

# class MovieSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()
#     class Meta:
#         model = Movie
#         # fields = ['name', 'description', 'is_active']
#         # exclude = ['is_active']
#         fields = "__all__"
#
#
#     def get_len_name(self, object): # get_"+ variable name"
#         length = len(object.name)
#         return length
#
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short')
#         else:
#             return value
#
#     #validator - object level
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and Description should be different')
#         return data

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(
#         read_only=True,
#     )
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     is_active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data): #instance carries old values, validated_data carries new values
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.save()
#         return instance
#
#     #validator - field level
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short')
#         else:
#             return value
#
#     #validator - object level
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and Description should be different')
#         return data
