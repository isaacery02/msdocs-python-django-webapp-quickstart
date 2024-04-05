from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host.startswith('pythonwebapptestisaac.azurewebsites.net'):  # Replace with your naked domain
            return HttpResponsePermanentRedirect(f'https://www.isaacsplex.com)

        response = self.get_response(request)
        return response