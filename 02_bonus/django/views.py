from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
        return HttpResponse("<h1>Hello , this is a django app for docker bonus part</h1><br><img src='https://www.docker.com/sites/default/files/social/docker_facebook_share.png'><h3> © Anas Benani</h3><style>h1,h3{text-align: center;margin-top: 100px; color: #0db7ed;}img{display: block;margin-left: auto;margin-right: auto;}</style>")

