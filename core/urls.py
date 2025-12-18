from django.urls import path
from .views import (
    AnnouncementListCreateView,
    AnnouncementDetailView,
    OpportunityListCreateView,
)

urlpatterns = [
    path('announcements/', AnnouncementListCreateView.as_view()),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view()),
    path('opportunities/', OpportunityListCreateView.as_view()),
]
