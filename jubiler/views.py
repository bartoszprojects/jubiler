from __future__ import unicode_literals
from django.views.generic import TemplateView
from slider.models import MainSlider, MiniSliderOfferIndividual, MiniSliderOfferRepair, MiniSliderOfferEngraving
from products.models import ProductsMini
from . forms import ContactForm

slides = MainSlider.objects.all()[0]
slides_mini_individual = MiniSliderOfferIndividual.objects.all()
slides_mini_repair = MiniSliderOfferRepair.objects.all()
slides_mini_engraving = MiniSliderOfferEngraving.objects.all()
products_mini = ProductsMini.objects.all()[:5]
form = ContactForm()

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        slides_list = []
        for elem in slides_mini_individual:
            if elem.image.url != '':
                slides_list.append(elem.image.url)

        context = super(IndexView, self).get_context_data(**kwargs)

        context['slides'] = slides
        context['products_mini'] = products_mini
        context['form'] = form
        context['slides_mini_individual'] = slides_mini_individual
        context['slides_mini_repair'] = slides_mini_repair
        context['slides_mini_engraving'] = slides_mini_engraving
        context['slides_list'] = slides_list

        return context



