import requests
from scrapy import Selector


SITE = "www.chapters.indigo.ca"


def check_stock(url):
    html = requests.get(url).content
    sel = Selector(text=html)
    stock_status = sel.css(
        "span.online-availability__availability-text::text").extract()

    # the html layout of 'in stock' and 'out of stock' are slightly different so we have to look for different tags
    if stock_status:
        stock_status = stock_status.get_text()
    else:
        stock_status = sel.css(
            "div.online-availability__shipping-message").extract().replace("Free shipping on orders over $35", "In stock")

    return stock_status


def check_price(url):
    html = requests.get(url).content
    sel = Selector(text=html)

    price = sel.css("span.item-price__price-amount::text")
    # the html layout of regular price and sale price are slightly different so we have to look for different tags
    if price:  # on sale
        price = price.extract()
    else:
        price = sel.css("div.item-price__normal::text").extract()

    return price


def get_product_name(url):
    html = requests.get(url).content
    sel = Selector(text=html)

    return sel.css("h1.product-title::text").extract()
