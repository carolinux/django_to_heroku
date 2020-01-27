from django.http import JsonResponse
from django.views import View
from django.views.generic.base import TemplateView



class News(View):
    """
    Return top N news in json format
    """
    def get(self, request):
        n = request.GET.get('n', 5)
        return JsonResponse({'news': []})


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        return context
