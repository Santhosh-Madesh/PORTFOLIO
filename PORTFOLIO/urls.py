from django.urls import path, re_path
from .views import home, LatestGitHubActivityAPIView, LatestGitHubProjectsAPIView, FrontendAppView

urlpatterns = [
    path('', home, name='home'),
    path('api/projects/', LatestGitHubProjectsAPIView.as_view(), name="projects"),
    path('api/events/', LatestGitHubActivityAPIView.as_view(), name='activity'),
    re_path(r'^.*$', FrontendAppView.as_view(), name='frontend'),
]