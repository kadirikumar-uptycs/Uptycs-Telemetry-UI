from django.shortcuts import render
import requests
import json
from datetime import datetime

# Create your views here.

def home(request):
    return render(request, 'homepage.html')

def aws(request):
    return render(request, 'AWS.html')


def gcp(request):
    return render(request, 'GCP.html')


def cloudTrail(request):
    response = requests.get(url='http://localhost:1729/getAWSCloudTrailEvents')

    data =json.loads(response.text)

    return render(request, 'cloudTrailEvents.html', {'events': data})


def ec2Instances(request):
    response = requests.get(url='http://localhost:1729/getAWSEC2Instances')

    data =json.loads(response.text)

    return render(request, 'Ec2.html', {'Instances' : data})


def s3Buckets(request):
    response = requests.get(url='http://localhost:1729/getAWSS3Buckets')

    data =json.loads(response.text)

    return render(request, 'S3.html', {'Buckets': data})

def iamDetails(request):
    policiesResponse = requests.get(url='http://localhost:1729/getAWSIAMPolicies')
    rolesResponse = requests.get(url='http://localhost:1729/getAWSIAMRoles')
    usersResponse = requests.get(url='http://localhost:1729/getAWSIAMUsers')

    policies = json.loads(policiesResponse.text)
    roles = json.loads(rolesResponse.text)
    users = json.loads(usersResponse.text)


    return render(request, 'IAM.html', {"Policies": policies, 'Roles' : roles, 'Users': users})


def vpcs(request):
    response = requests.get(url='http://localhost:1729/getAWSVPCs')

    data = json.loads(response.text)

    return render(request, 'VPC.html',{'VPCs' : data})


def storage(request):
    response = requests.get(url='http://localhost:1729/getGCPBuckets')

    data = json.loads(response.text)

    return render(request, 'Storage.html', {'Buckets' : data})


def computeEngine(request):
    response = requests.get(url='http://localhost:1729/getGCPComputeEngines')

    data = json.loads(response.text)

    return render(request, 'ComputeEngine.html', {'ComputeEngines' : data})


def cloudFunction(request):
    response = requests.get(url='http://localhost:1729/getGCPCloudFunctions')

    data = json.loads(response.text)

    return render(request, 'cloudFunction.html', {'CloudFunctions' : data})