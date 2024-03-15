from rest_framework import serializers
from admin_tools.models import Report, Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
