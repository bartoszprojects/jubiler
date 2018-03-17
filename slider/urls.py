from django.urls import path
from . views import MiniSliderOfferIndividualData, MainSliderData

urlpatterns = [
    path('mini_slides_ind', MiniSliderOfferIndividualData.as_view()),
    path('main_slider', MainSliderData.as_view())
]





