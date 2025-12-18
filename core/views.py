from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from django.utils.timezone import now
from .models import Announcement, Opportunity
from .serializers import AnnouncementSerializer, OpportunitySerializer
from accounts.permissions import IsAdminUserProfile

class AnnouncementListCreateView(ListCreateAPIView):
    queryset = Announcement.objects.all().order_by('-created_at')
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        if self.request.user.profile.role != 'admin':
            raise PermissionError("Not allowed")
        serializer.save(created_by=self.request.user)


class AnnouncementDetailView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class OpportunityListCreateView(ListCreateAPIView):
    serializer_class = OpportunitySerializer

    def get_queryset(self):
        return Opportunity.objects.filter(
            verified=True,
            deadline__gte=now().date()
        ).order_by('deadline')

    def perform_create(self, serializer):
        if self.request.user.profile.role != 'admin':
            raise PermissionError("Not allowed")
        serializer.save(created_by=self.request.user)
