from rest_framework import serializers
from .models import Announcement, Opportunity

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at']


class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'
        read_only_fields = ['created_by', 'verified', 'created_at']
