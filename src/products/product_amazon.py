from lxml import html
# beautiful soup doesn't work for amazon for some reason
from urllib.request import urlopen
import urllib.error
import time
import requests


SITE = "www.amazon.ca"

# lxml.html.parse will sometimes throw HTTPError, so wrap the parsing in a loop to retry


def check_stock(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    print(url)
    print(tree)
    element = tree.xpath("//div[@id='availabilityInsideBuyBox_feature_div']")
    print("check_stock")
    print(element)
    print(url)
    if len(element) > 0:
        element = element[0]
    return element.text_content()


def check_price(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    element = tree.xpath(
        "//div[@id='corePrice_desktop']//span[contains(@class,'a-price')]/span[@class='a-offscreen']")
    print("price")
    print(element)
    print(url)
    if len(element) > 0:
        element = element[0]
    return element.text_content()


def get_product_name(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    element = tree.xpath("//span[@id='productTitle']")
    print("name")
    print(element)
    print(url)
    if len(element) > 0:
        element = element[0]
    return element.text_content()
