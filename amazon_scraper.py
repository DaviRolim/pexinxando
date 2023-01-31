import requests
from bs4 import BeautifulSoup
from time import sleep
import random

BASE_URL = "https://www.amazon.com.br"

# List of User-Agent strings to rotate
user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
]

def build_url(search_term):
    return BASE_URL + "/s?k=" + search_term.replace(" ", "+")


def scrape(product):
    FINAL_URL = build_url(product)
    print(f'Buscando {product} em {FINAL_URL}')
    headers = {'User-Agent': random.choice(user_agents)}
    page = requests.get(FINAL_URL, headers=headers)
    # with open('bsoupplayground.html', 'r') as f:
    # page = f.read()
    soup = BeautifulSoup(page.content, "html.parser")
    # get a random time between 5 and 10 seconds
    sleep_time = random.randint(5, 10)
    sleep(sleep_time)
    # I don't need to get the link for the product as I dont need to enter the page
    # I only need the product name, number of reviews and the price
    product_cards = soup.findAll('div', {'class': 's-card-container'})
    products = []
    for product in product_cards[:3]:
        product_title = product.find(
            'span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).text.strip()
        print(product_title)

        # build price from the spans
        product_price = product.find('span', {'class': 'a-price-whole'})
        if not product_price:
            continue
        product_price = product_price.text.strip()
        product_price += product.find('span',
                                      {'class': 'a-price-fraction'}).text.strip()
        print(product_price)

        product_stars = product.find(
            'span', {'class': 'a-icon-alt'}).text.strip()
        print(product_stars)

        product_link = product.find('a', {'class': 'a-link-normal s-no-outline'})
        if not product_link:
            continue
        product_link = BASE_URL + product_link['href']

        product_number_of_reviews = product.find(
            'span', {'class': 'a-size-base s-underline-text'}).text.strip()
        print(product_number_of_reviews)
        print('-----------------')
        products.append({
            'title': product_title,
            'price': product_price,
            'stars': product_stars,
            'number_of_reviews': product_number_of_reviews,
            'link': product_link,
        })
    return products
