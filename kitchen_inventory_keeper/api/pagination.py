from rest_framework.settings import api_settings
from rest_framework.response import Response
from collections import OrderedDict
from django.db.models import Q

from rest_framework.pagination import LimitOffsetPagination


class ProceduresPagePagination:
    def __init__(self, request):
        try:
            self.limit = int(request.query_params.get("limit", api_settings.PAGE_SIZE))
        except ValueError:
            self.limit = 50

        try:
            self.offset = int(request.query_params.get("offset", 0))
        except ValueError:
            self.offset = 0

        self.max_limit = 100

        if self.limit is None:
            self.limit = 50
        elif self.limit > self.max_limit:
            self.limit = self.max_limit

        self.request = request
        self.limit_query_param = "limit"
        self.offset_query_param = "offset"

    def get_paginated_response(self, data):
        return {
            "next_offset": self.get_next_offset(data),
            "previous_offset": self.get_previous_offset(),
            "results": data,
        }

    def get_next_offset(self, data):
        # if self.offset + self.limit >= self.count:
        #    return None

        if len(data) < self.limit:
            return None

        return self.offset + self.limit

    def get_previous_offset(self):
        if self.offset <= 0:
            return None

        if self.offset - self.limit <= 0:
            return 0

        return self.offset - self.limit


class CustomLimitOffsetPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("count", self.count),
                    ("next_offset", self.get_next_offset()),
                    ("previous_offset", self.get_previous_offset()),
                    ("results", data),
                ]
            )
        )

    def get_next_offset(self):
        if self.offset + self.limit >= self.count:
            return None

        return self.offset + self.limit

    def get_previous_offset(self):
        if self.offset <= 0:
            return None

        if self.offset - self.limit <= 0:
            return 0

        return self.offset - self.limit
