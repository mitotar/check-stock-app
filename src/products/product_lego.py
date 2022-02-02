import requests
from scrapy import Selector


SITE = "www.lego.com"


def check_stock(url):
    html = requests.get(url).content
    sel = Selector(text=html)
    stock = sel.xpath(
        "//p[@data-test='product-overview-availability']/span/text()").extract()[0]
    return stock


def check_price(url):
    html = requests.get(url).content
    sel = Selector(text=html)

    price = sel.xpath("//span[@data-test='product-price-sale']/text()")
    if price:  # sale price
        price = price.extract().replace("Sale Price", "$")
    else:
        price = sel.xpath("//span[@data-test='product-price']/text()")[0]
        if price:  # regular price
            price = "$" + price.extract()
        else:  # no price (retired product)
            price = "--------------"

    return price


def get_product_name(url):
    html = requests.get(url).content
    sel = Selector(text=html)

    return sel.xpath("//h1[@data-test='product-overview-name']/span/text()").extract()
