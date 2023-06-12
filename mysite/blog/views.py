from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'blog/index.html'

def method_a():
    print('method_a')
    print('r4')
    return 'done'

def method_aa():
    print('pick me')

def method_aaa():
    pass

def method_aaaa():
    pass
