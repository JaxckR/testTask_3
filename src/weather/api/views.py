from rest_framework.generics import ListAPIView

from weather.api.pagination import RegionPagination
from weather.api.serializers import RegionSerializer
from weather.models import RegionHistory


class RegionView(ListAPIView):
    '''Класс отображения статистики по переходам по городам

    Используемый сериализатор: RegionSerializer
    Используемый класс пагинации: RegionPagination
    Значения берутся из модели RegionHistory
    '''
    serializer_class = RegionSerializer
    queryset = RegionHistory.objects.all()
    pagination_class = RegionPagination
