from django.views.generic import TemplateView

from urllib.parse import quote, unquote

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

    В методе get реализовано сохранение последнего просмотренного города в
    cookie с временем истечения 7 дней
    '''
    template_name = 'weather/index.html'

    def get(self, request, *args, **kwargs):
        if not request.GET.get('city'):
            return super().get(request, *args, **kwargs)

        response = super().get(request, *args, **kwargs)
        response.set_cookie("last_city", quote(request.GET.get('city')), expires=60 * 60 * 24 * 7)
        return response

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        if last_city := self.request.COOKIES.get("last_city"):
            context["last_city"] = unquote(last_city)

        if city := self.request.GET.get('city'):
            forecast_city_data = get_current_forecast_weather(city)

            if error := forecast_city_data.get('error'):
                context["error"] = error
                return context

            for key, value in forecast_city_data["current"].items():
                context[key] = value

            context['forecast'] = [forecast_city_data["forecast"]]
        return context
