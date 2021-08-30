from rest_framework.pagination import PageNumberPagination


class WatchListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    page_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'
