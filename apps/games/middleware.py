from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin


class JavaScriptContentTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)

        if response.status_code == 200 and request.path.endswith('.js'):
            response["Content-Type"] = "text/javascript"
        return response
