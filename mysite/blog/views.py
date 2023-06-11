from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'blog/index.html'

def method_a():
    print('method_a')
    print('r1')
    return 'done'
