from rest_framework.serializers import ModelSerializer

from weather.models import RegionHistory


class RegionSerializer(ModelSerializer):
    '''Класс-сериализатор для вывода статистики перехода по регионам

    Возвращаемые значения:
        - region: str
        - count: int
    '''
    class Meta:
        model = RegionHistory

        fields = ["region", "count"]
