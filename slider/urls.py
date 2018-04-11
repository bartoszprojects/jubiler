from django.urls import path
from .views import MiniSliderOfferIndividualData, MiniSliderOfferEngravingData, MiniSliderOfferRepairData, \
    MainSliderData, AboutInformationsSerializerData

urlpatterns = [
    path('mini_slides_ind', MiniSliderOfferIndividualData.as_view()),
    path('mini_slides_engraving', MiniSliderOfferEngravingData.as_view()),
    path('mini_slides_repair', MiniSliderOfferRepairData.as_view()),
    path('main_slider', MainSliderData.as_view()),
    path('about_informations', AboutInformationsSerializerData.as_view())
]
