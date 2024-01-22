from django.urls import path

from profile_app.views import ProfileListCreateView, ProfileDetailView

urlpatterns = [
    path('data/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('data/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]