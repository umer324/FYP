from rest_framework import serializers
from users_api import models

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.UserProfile
        fields=('id','email','name','role','password')
        extra_kwargs={
            'password':{
                'style':{'input_type':'password'}
            }
        }

    def create(self,validated_data):
        user=models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            role=validated_data['role'],
            password=validated_data['password']
        )


        return user


class Packaging_lineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Packaging_line
        fields = ['line_id', 'description']


class Line_control_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Line_control_details
        fields = ['id','user_id', 'line_id']


class Batch_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Batch_details
        fields = ['test_id', 'start_dateTime', 'end_datetime', 'line_id', 'user_id']


class Batch_Test_resultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Batch_Test_results
        fields = ['strip_id', 'result_status', 'test_id']

