from rest_framework.pagination import PageNumberPagination


class RegionPagination(PageNumberPagination):
    '''Класс пагинации для отображения статистики перехода по городам

    Возможна установка произвольного объема выдаваемых данных вплоть до 1000 за запрос
    Установка произвольного объема выдаваемых данных происходит при помощи query параметра
    page_size

    Переход по страницам осуществляется при помощи query параметра page
    '''
    page_size = 100
    max_page_size = 1000
    page_size_query_param = 'page_size'
    page_query_param = 'page'
