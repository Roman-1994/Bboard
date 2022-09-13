from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from bb_ap.models import Bb


class BbPagination(PageNumberPagination):
    page_size = 3


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BbFilter(filters.FilterSet):
    rubric = CharFilterInFilter(field_name='rubric__name', lookup_expr='in')
    price = filters.RangeFilter()

    class Meta:
        model = Bb
        fields = ['rubric', 'price']

