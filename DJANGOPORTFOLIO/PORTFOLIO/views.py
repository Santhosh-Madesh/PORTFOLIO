from this import d
from django.shortcuts import render
from django.conf import settings
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView
import os
from django.conf import settings


class FrontendAppView(TemplateView):
    template_name = "index.html"

    def get_template_names(self):
        return [os.path.join(settings.BASE_DIR, "frontend/build/index.html")]


class LatestGitHubProjectsAPIView(APIView):

    def get(self, request):

        username = settings.GITHUB_USERNAME
        url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=6"

        response = requests.get(url)

        if response.status_code == 200:
            repos = response.json()
        else:
            repos = []

        return Response({"repos":repos})

class LatestGitHubActivityAPIView(APIView):

    def get(self, request):

        username = settings.GITHUB_USERNAME
        url = f"https://api.github.com/users/{username}/events/public"

        event_response = requests.get(url)

        if event_response.status_code == 200:
            events = event_response.json()[:5]
        else:
            events = []

        return Response({"events":events})
        

def latest_github_projects():

    username = settings.GITHUB_USERNAME
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=4"

    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
    else:
        repose = []

    return repos

def latest_github_activities():

    username = settings.GITHUB_USERNAME
    event_url = f"https://api.github.com/users/{username}/events/public"

    try:
        event_response = requests.get(event_url)
        event_response.raise_for_status()
        events = event_response.json()[:5]
    
    except requests.exceptions.RequestException:

        events = []

    activity = []

    for e in events:

        event_type = e.get('type')
        repo_name = e.get('repo', {}).get('name')
        created_at = e.get('created_at')

        activity.append(
            {
                "type":event_type,
                "repo":repo_name,
                "data":created_at
            }
        )

        return activity

def home(request):
    repos = latest_github_projects()
    activity = latest_github_activities()

    return render(request, 'index.html', {"repos":repos, "activity":activity})


