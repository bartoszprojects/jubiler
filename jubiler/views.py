from __future__ import unicode_literals
from django.views.generic import TemplateView
from slider.models import MainSlider
from products.models import ProductsMini

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        slides = MainSlider.objects.all()[0]
        context = super(IndexView, self).get_context_data(**kwargs)
        context['slides'] = slides
        return context


