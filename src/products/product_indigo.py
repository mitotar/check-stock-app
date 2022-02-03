import requests
from scrapy import Selector


SITE = "www.chapters.indigo.ca"


def check_stock(url):
    print(url)
    html = requests.get(url).content
    sel = Selector(text=html)
    return sel.css(
        "div.online-availability__shipping-message span::text")[0].extract()


def check_price(url):
    html = requests.get(url).content
    sel = Selector(text=html)

    price = sel.css("span.item-price__price-amount::text")
    # the html layout of regular price and sale price are slightly different so we have to look for different tags
    if price:  # on sale
        price = price[0].extract()
    else:
        price = sel.css("div.item-price__normal::text")[0].extract()

    return price


def get_product_name(url):
    html = requests.get(url).content
    sel = Selector(text=html)

    return sel.css("h1.product-title::text")[0].extract()
