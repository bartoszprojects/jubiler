from django.contrib import admin
from . models import MainSlider, MiniSliderOfferEngraving, MiniSliderOfferIndividual, MiniSliderOfferRepair,\
    AboutInformations, Service, ServiceImages
# Register your models here.
admin.site.register(MiniSliderOfferEngraving)
admin.site.register(MiniSliderOfferIndividual)
admin.site.register(MiniSliderOfferRepair)

from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = AboutInformations
        fields = ('title', 'content',)

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(AboutInformations, PostAdmin)

class ServiceImagesInline(admin.StackedInline):
    model = ServiceImages
    fields = ['image', ]

class ServicesAdmin(admin.ModelAdmin):
    inlines = [
        ServiceImagesInline,
    ]

admin.site.register(Service, ServicesAdmin)