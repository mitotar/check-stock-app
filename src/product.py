from src.web_helper import get_site_name
import src.products.indigo_product as indigo
import src.products.lego_product as lego


def create_product(url):
    site = get_site_name(url)

    if site == indigo.SITE:
        name = indigo.get_product_name(url)
    elif site == lego.SITE:
        name = lego.get_product_name(url)

    return [site, name]


def check_stock(site, url):
    if site == indigo.SITE:
        return indigo.check_stock(url)
    elif site == lego.SITE:
        return lego.check_stock(url)
