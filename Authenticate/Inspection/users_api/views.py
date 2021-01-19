from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status,viewsets
from rest_framework.response import Response
from users_api import serializers
from users_api import models,permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response=super(CustomObtainAuthToken,self).post(request,*args,**kwargs)
        token=Token.objects.get(key=response.data['token'])
        print(token.user_id)
        user=models.UserProfile.objects.get(id=token.user_id)
        return Response({'token':token.key,'user':serializers.UserProfileSerializer(user).data})


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    #spermission_classes = (permissions.UpdateOwnProfile,)

class PackagingLineViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.Packaging_lineSerializer
    queryset = models.Packaging_line.objects.all()



class Line_control_detailsViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.Line_control_detailsSerializer
    queryset = models.Line_control_details.objects.all()


class Batch_detailsViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.Batch_detailsSerializer
    queryset = models.Batch_details.objects.all()



class Batch_Test_resultsViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.Batch_Test_resultsSerializer
    queryset = models.Batch_Test_results.objects.all()




class UserLoginApiView(CustomObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES






@csrf_exempt
def states(request):

    if request.method == 'GET':
        valid =len(models.Batch_Test_results.objects.filter(result_status='valid'))
        invalid=len(models.Batch_Test_results.objects.filter(result_status='invalid'))
        total=len(models.Batch_Test_results.objects.all())
        data={
            "total":total,
            "valid":valid,
            "invalid":invalid
        }

        return JsonResponse(data, safe=False)


@csrf_exempt
def lenUser(request):
    """
    List all code articles, or create a new Article.
    """
    if request.method == 'GET':
        supervisor=len(models.UserProfile.objects.filter(role='supervisor'))
        inspector =len(models.UserProfile.objects.filter(role='inspector'))
        admin=len(models.UserProfile.objects.filter(role='admin'))
        total=len(models.UserProfile.objects.all())
        data={
            "total":total,
            "admin":admin,
            "supervisor":supervisor,
            "inspector":inspector
        }

        return JsonResponse(data, safe=False)


