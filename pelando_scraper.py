import requests
from bs4 import BeautifulSoup


URL = "https://www.pelando.com.br/"
page = requests.get(URL)
BAIT_WORDS = ['ganhe', 'cupon', 'gratis', 'cashback']

soup = BeautifulSoup(page.content, "html.parser")

def scrape():
    product_div = soup.findAll('div', {'class': 'pf7gf4-0'})
    products = []

    for div in product_div:
        # find the product name
        product_name = div.find_next('a', {'class': 'l42owz-4'}).text
        if any(word in BAIT_WORDS for word in product_name.lower().split()):
            continue
        
        # find the product price
        product_price = div.find_next('span', {'class': 'sc-4ay64u-0'})\
            .find_next('span')\
            .get_text()\
            .strip()
        if product_price == 'Grátis':
            product_price = '0'
        product_price = product_price.replace(',', '.')

        # find the product temperature
        product_temperature = div.find_next('span', {'class': 'dqqirw-0'}).text.replace('º', '')

        # find the store selling the product
        product_seller = div.find_next('a', {'class': 'pf7gf4-4'}).text

        # add to products array
        products.append({
            'name': product_name,
            'offer_price': product_price,
            'temperature': product_temperature,
            'seller': product_seller
        })
    products_sorted_by_temperature = sorted(products, key=lambda x: float(x['temperature']), reverse=True)
    return products_sorted_by_temperature
