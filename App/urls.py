from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('aws', views.aws),
    path('gcp', views.gcp),
    path('cloudTrailEvents', views.cloudTrail),
    path('ec2Instances', views.ec2Instances),
    path('s3Buckets', views.s3Buckets),
    path('iam', views.iamDetails),
    path('vpc', views.vpcs),
    path('storages', views.storage),
    path('computeEngines', views.computeEngine),
    path('cloudFunctions', views.cloudFunction)
]