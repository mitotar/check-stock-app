from ..web_helper import get_site_name
from . import product_indigo as indigo
from . import product_lego as lego


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
