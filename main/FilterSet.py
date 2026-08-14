import django_filters
from .models import Review



class ReviewFilter(django_filters.FilterSet):

    min_age=django_filters.NumberFilter(
        field_name="rate",
        lookup_expr="gte"
    )

    max_age=django_filters.NumberFilter(
        field_name="rate",
        lookup_expr="lte"
    )

    class Meta:
        model=Review
        fields=['min_age','max_age']