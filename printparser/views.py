from django.http import HttpResponse
from django.views import View
from printparser.parser import get_item_urls, save_item_details, update_prints


class ScrapeFactorio(View):

    def scrape_all(self):
        item_list = get_item_urls()
        save_item_details(item_list, None)
        return HttpResponse("Prints are scraped and saved to DataBase")

    def update_all(self):
        update_prints()
        return HttpResponse("Completed Updating prints")
