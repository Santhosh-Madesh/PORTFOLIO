from django.urls import path
from .views import home, LatestGitHubActivityAPIView, LatestGitHubProjectsAPIView

urlpatterns = [
    path('', home, name='home'),
    path('api/projects/', LatestGitHubProjectsAPIView.as_view(), name="projects"),
    path('api/events/', LatestGitHubActivityAPIView.as_view(), name='activity')
]