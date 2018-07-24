"""jubiler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import slider.urls, products.urls
import ckeditor_uploader.urls
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('slides/', include(slider.urls)),
    path('products/', include(products.urls)),
    path('ckeditor/', include(ckeditor_uploader.urls)),

    path('', TemplateView.as_view(template_name="index.html")),
    path('about.html', TemplateView.as_view(template_name="about.html")),
    path('home.html', TemplateView.as_view(template_name="home.html")),
    path('image.html', TemplateView.as_view(template_name="image.html")),
    path('index.html', TemplateView.as_view(template_name="index.html")),
    path('main_slider.html', TemplateView.as_view(template_name="main_slider.html")),
    path('mini_slider.html', TemplateView.as_view(template_name="mini_slider.html")),
    path('navbar.html', TemplateView.as_view(template_name="navbar.html")),
    path('products_category.html', TemplateView.as_view(template_name="products_category.html")),
    path('products.html', TemplateView.as_view(template_name="products.html")),
    path('services.html', TemplateView.as_view(template_name="services.html")),
    path('slider.html', TemplateView.as_view(template_name="slider.html")),
    path('product.html', TemplateView.as_view(template_name="product.html")),
    path('terms.html', TemplateView.as_view(template_name="terms.html")),
    path('image_modal.html', TemplateView.as_view(template_name="image_modal.html")),
    path('mini_product.html', TemplateView.as_view(template_name="mini_product.html")),
    path('mini_products_slider_template.html', TemplateView.as_view(template_name="mini_products_slider_template.html")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
