from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
#CURSOR - we do not have a page number but we do have buttons for 'next' and 'previous'
# by default we depend on ordering of time "created"

class WatchListPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'records' #by default it takes 'page'
    page_size_query_param = 'size'#take the page size from the customer
    max_page_size = 20
    # last_page_strings = 'end' #by default it is set as 'last'


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start' #replaces offset with start in the URL


class WatchlistCPagination(CursorPagination): #when we want our user to read all the information provided (i.e. Terms and Conditions)
    page_size = 5
    ordering = 'created' #old to new; by default it is '-created'
    cursor_query_param = 'record'