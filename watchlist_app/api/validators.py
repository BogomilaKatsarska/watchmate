from rest_framework import serializers


def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name is too short')