import requests

from django.http import JsonResponse
from django.views import View
from django.views.generic.base import TemplateView

from news_ticker import settings

class News(View):
    """
    Return top N news titles in json format
    """
    def get(self, request):
        n = request.GET.get('n', 5)
        guardian_url = "https://content.guardianapis.com/search?api-key={}&page-size={}".format(settings.GUARDIAN_API_KEY, n)
        resp = requests.get(guardian_url)
        resp_json = resp.json()
        return JsonResponse({'titles': [{"title":article['webTitle'], "url":article['webUrl']} for article in resp_json['response']['results']]})


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        return context
