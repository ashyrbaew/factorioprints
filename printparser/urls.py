from django.urls import path
from printparser.views import ScrapeFactorio


app_name = 'printparser'

urlpatterns = [
    path('parse', ScrapeFactorio.scrape_all, name='parser'),
    path('update', ScrapeFactorio.update_all, name='update'),
]