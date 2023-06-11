from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'blog/index.html'

def method_a():
    print('method_a')
    return 'done'

def method_aa():
    pass

def method_aaa():
    pass
