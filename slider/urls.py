from django.urls import path
from . views import MiniSliderOfferIndividualData, MiniSliderOfferEngravingData, MiniSliderOfferRepairData, MainSliderData

urlpatterns = [
    path('mini_slides_ind', MiniSliderOfferIndividualData.as_view()),
    path('mini_slides_engraving', MiniSliderOfferEngravingData.as_view()),
    path('mini_slides_repair', MiniSliderOfferRepairData.as_view()),
    path('main_slider', MainSliderData.as_view())
]





