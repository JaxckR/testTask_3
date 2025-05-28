from django.test import TestCase
from django.urls import reverse

from weather.api_requests.weather import get_current_weather, get_current_forecast_weather


class WeatherTestCase(TestCase):
    def setUp(self):
        ...

    def tearDown(self):
        ...

    def test_indexPage_without_data(self):
        path = reverse("home")
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "weather/index.html")

    def test_indexPage_with_correct_data(self):
        path = reverse("home")
        response = self.client.get(f"{path}?city=Moscow")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "weather/index.html")
        self.assertIn("city", response.context_data)
        self.assertIn("temp", response.context_data)
        self.assertIn("text", response.context_data)
        self.assertIn("forecast", response.context_data)

    def test_indexPage_with_incorrect_data(self):
        path = reverse("home")
        response = self.client.get(f"{path}?city=asfdasbhjafs")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "weather/index.html")
        self.assertIn("error", response.context_data)

    def test_get_current_weather(self):
        result = get_current_weather("Moscow")
        self.assertEqual(type(result), dict)
        self.assertIn("city", result)
        self.assertIn("temp", result)
        self.assertIn("text", result)
        self.assertEqual(result["city"], "Moscow")

    def test_get_current_forecast_weather(self):
        result = get_current_forecast_weather("Moscow")
        self.assertEqual(type(result), dict)
        self.assertIn("current", result)
        self.assertIn("city", result["current"])
        self.assertIn("temp", result["current"])
        self.assertIn("text", result["current"])
        self.assertIn("forecast", result)
        self.assertEqual(result["current"]["city"], "Moscow")
        self.assertEqual(len(result["forecast"]), 7)


class WeatherAPITestCase(TestCase):
    fixtures = ["mock_data.json"]

    def setUp(self):
        ...


    def tearDown(self):
        ...


    def test_region_statistics(self):
        path = reverse("regions_statistics")
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 6)

    def test_region_statistics_pagination(self):
        path = reverse("regions_statistics")
        response = self.client.get(f"{path}?page_size=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 6)
        response = self.client.get(response.data["next"])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 6)
        self.assertEqual(len(response.data["results"]), 1)
