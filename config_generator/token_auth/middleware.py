from config_generator.configurator.models import WhiteLabel
from django.utils.deprecation import MiddlewareMixin
from django.http import Http404
from django.core.exceptions import PermissionDenied


class RequestAuth(MiddlewareMixin):

    def process_response(self, request, response, *args):
        if 'Authorization' in request.headers:

            app = request.GET.get('app')

            try:
                token_type, refresh_token = request.headers['Authorization'].split(' ')
            except:
                token_type, refresh_token = '', ''

            app = WhiteLabel.objects.filter(slug=app).first()

            if app:
                if token_type == 'Bearer':
                    if str(app.api_key) == refresh_token:
                        return response
                    else:
                        raise PermissionDenied("Wrong token!")
                else:
                    raise PermissionDenied("Token is incorrect!")
            else:
                raise Http404("WhiteLabel does not exist")

        return response
