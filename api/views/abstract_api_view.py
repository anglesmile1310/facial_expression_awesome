from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from api.helpers.response_format import json_format

class AbstractAPIView(APIView):
    """
        The abstract view of any views in API.
        You can extend this view for each use case.
    """
    parser_classes = (MultiPartParser, JSONParser)

    def json_format(self, code = None, data = None, message = None, errors = None):
        return json_format(code=code, data=data,message=message, errors=errors)
