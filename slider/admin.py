from django.contrib import admin
from . models import MainSlider, MiniSliderOfferEngraving, MiniSliderOfferIndividual, MiniSliderOfferRepair,\
    AboutInformations, Service, ServiceImages
# Register your models here.
admin.site.register(MiniSliderOfferEngraving)
admin.site.register(MiniSliderOfferIndividual)
admin.site.register(MiniSliderOfferRepair)
admin.site.register(Service)
admin.site.register(ServiceImages)



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