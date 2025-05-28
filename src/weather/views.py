from django.views.generic import TemplateView

from weather.api_requests.weather import get_current_forecast_weather


class IndexPage(TemplateView):
    '''Основной класс данного проекта.

    Возвращает пустую страницу если не передан query аргумент city,
    в ином случае возвращает данные о погоде либо ошибку(не найден город)

    Возвращаемый html файл находится в weather/templates/weather/index.html
    Используемый context:
        - name: str
        - icon: str
        - temp: float
        - text: str
        - forecast: list[dict] с ключом day: int и значением dict
    '''
    template_name = 'weather/index.html'

    def __init__(self, *args, **kwargs):
        self.forecast_city_data = {}
        super().__init__(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if city := request.GET.get('city'):
            self.forecast_city_data = get_current_forecast_weather(city)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        if self.forecast_city_data:
            for key, value in self.forecast_city_data["current"].items():
                context[key] = value

            context['forecast'] = [self.forecast_city_data["forecast"]]
        return context
