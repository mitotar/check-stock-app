import requests
from scrapy import Selector


SITE = "www.boardgamebliss.com"


def check_stock(url):
    html = requests.get(url).content
    sel = Selector(text=html)
    return sel.css(
        "span.product-form__inventory::text")[0].extract()


def check_price(url):
    html = requests.get(url).content
    sel = Selector(text=html)

    return sel.css("span.price::text")[0].extract()


def get_product_name(url):
    html = requests.get(url).content
    sel = Selector(text=html)

    return sel.css("h1.product-meta__title::text")[0].extract()
