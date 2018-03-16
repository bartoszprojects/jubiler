from django.urls import path
from .views import MiniSliderOfferIndividualData

urlpatterns = [
    path('mini_slides_ind/', MiniSliderOfferIndividualData.as_view())
]


