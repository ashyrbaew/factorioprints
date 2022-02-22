from time import sleep
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from printparser.models import Prints

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://factorioprints.com/top/")
driver.implicitly_wait(10)


def get_item_urls():
    item_url_list = []
    max_page = 2
    last_page = 0

    while last_page < max_page:
        last_page += 1
        next_page_button_xpath = "//*[contains(text(), 'Next Page')]"
        button = driver.find_elements(By.XPATH, next_page_button_xpath)
        page_links = driver.find_elements(By.XPATH, "//*[contains(@class, 'container-fluid')]/div[3]//a")
        for lnk in page_links:
            item_url_list.append(lnk.get_attribute("href"))

        try:
            button[0].send_keys(u'\ue006')  # to click next_page button
            sleep(1)
        except IndexError:
            break

    return list(set(item_url_list))


def save_item_details(item_url_list, item_key):
    item = Prints.objects.filter(key=item_key)

    def write_to_db(model_item):
        driver.find_elements(By.XPATH, "//*[contains(@class, 'card')]//*[contains(@class, 'card-body')]/button[2]")[0].send_keys(u'\ue006')
        model_item.image = driver.find_elements(By.XPATH, "//*[@class='col-md-4']/a/img")[0].get_attribute('src')
        model_item.details = driver.find_elements(By.XPATH,"//*[contains(@class, 'card')]//*[contains(@class, 'card-body')]/div")[0].text
        model_item.author = driver.find_elements(By.XPATH, "//div['card']/table/tbody/tr[1]/td[2]")[0].text
        model_item.created_at = driver.find_elements(By.XPATH,"//div['card']/table/tbody/tr[2]/td[2]/span")[0].get_attribute("title")
        model_item.updated_at = driver.find_elements(By.XPATH, "//div['card']/table/tbody/tr[3]/td[2]/span")[0].get_attribute("title")
        model_item.favorites = driver.find_elements(By.XPATH, "//div['card']/table/tbody/tr[4]/td[2]")[0].text
        model_item.blueprint = driver.find_elements(By.XPATH, "//div[@class='card-body']/div[@class='blueprintString']")[0].text
        model_item.save()

    if item:
            item.key = item_key
            driver.get(f'http://factorioprints.com/view/{item_key}')
            write_to_db(item)
    else:
        for lnk in item_url_list:
            item = Prints()
            driver.get(lnk)
            item.key = lnk.split("/")[-1]
            write_to_db(item)


def update_prints():
    items_in_db = list(Prints.objects.values_list('key', flat=True))
    item_urls_from_web = get_item_urls()

    for item in item_urls_from_web:
        key = item.split("/")[-1]
        if key not in items_in_db:
            save_item_details([item], key)
        else:
            items_in_db.remove(key)

    Prints.objects.filter(key__in=items_in_db).delete()
    return HttpResponse("total_items_link")

