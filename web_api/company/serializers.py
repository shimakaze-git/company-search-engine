from .models import Company
from rest_framework.serializers import ModelSerializer


class CompanySearchSerializer(ModelSerializer):
    class Meta:
        model = Company
        # fields = "__all__"
        fields = (
            "name",
            "name_kana",
            "description",
            "corporate_name",
            "foundation_date",
            "address",
            "url",
        )
        # exclude = ("created_at", "updated_at", "is_removed")
