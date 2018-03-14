from __future__ import unicode_literals
from django.views.generic import TemplateView
from slider.models import MainSlider
from products.models import ProductsMini
from . forms import ContactForm

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        slides = MainSlider.objects.all()[0]
        products_mini = ProductsMini.objects.all()[:5]
        form = ContactForm()

        context = super(IndexView, self).get_context_data(**kwargs)

        context['slides'] = slides
        context['products_mini'] = products_mini
        context['form'] = form
        return context


