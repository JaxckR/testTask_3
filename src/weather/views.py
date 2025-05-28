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

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        if city := self.request.GET.get('city'):
            forecast_city_data = get_current_forecast_weather(city)

            if error := forecast_city_data.get('error'):
                context["error"] = error
                return context

            for key, value in forecast_city_data["current"].items():
                context[key] = value

            context['forecast'] = [forecast_city_data["forecast"]]
        return context
