import operator
from functools import reduce
from typing import List

from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySearchSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.filter()
    serializer_class = CompanySearchSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        """
        企業個別の情報を取得する.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanySearchView(ListAPIView):
    queryset = Company.objects.filter(is_removed=False).order_by('-created_at')
    serializer_class = CompanySearchSerializer
    permission_classes = [AllowAny]
    # authentication_classes = (CustomTokenAuthentication, )

    @swagger_auto_schema(
        operation_description="GETリクエストを受け付けて、企業の情報を検索する.",
        responses={200: ""},
    )
    def list(self, request):

        queryset = self.get_queryset()
        values = queryset.values()
        print('values', values)

        keyword = request.query_params.get("keyword")
        if keyword:
            search_words = keyword.replace('　', ' ').split()

            filter_set = self.get_filter_set(search_words)
            query = self.get_query(filter_set)

            results = queryset.filter(query)
            companies = [
                self.get_serializer(result).data for result in results
            ]

            response_data = {"companies": companies}
            return Response(response_data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_filter_set(self, search_words: List):

        # 部分一致
        # __contains
        # filter_set = (
        #     Q(name__contains=w) |
        #     Q(name_kana__contains=w)
        #     for w in search_words
        # )

        # 前方一致
        # __istartswith
        filter_set = (
            Q(name__istartswith=w) |
            Q(name_kana__istartswith=w)
            for w in search_words
        )

        return filter_set

    def get_query(self, filter_set):
        query = reduce(operator.or_, filter_set)
        # query = reduce(operator.and_, search_params)

        return query
