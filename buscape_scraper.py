import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.buscape.com.br"
search_term = "Caixa Para Ferramentas Tatica Camper 44x23x18cm Metasul"
def build_url(search_term):
    return BASE_URL + "/search?q=" + search_term.replace(" ", "%20")

def is_affiliate_link(link):
    return 'buscape' in link

def scrape(product):
    if 'buscape' not in product:
        FINAL_URL = build_url(product)
    print(f'Buscando {product} em {FINAL_URL}...')

    page = requests.get(FINAL_URL)
    soup = BeautifulSoup(page.content, "html.parser")
    # find the product link that is a anchor tag with this class SearchCard_ProductCard_Inner__7JhKb
    product_page = soup.find('a', {'class': 'SearchCard_ProductCard_Inner__7JhKb'})
    if product_page is None:
        return []

    # Is there price comparison for this project?
    price_comparison_p = product_page.find_next('p', {'class': 'SearchCard_ProductCard_StoreCount__WamUx'})
    print(f'price comparison p {price_comparison_p}')
    if price_comparison_p is None or is_affiliate_link(product_page['href']):
        # Get single price and return
        single_price = product_page.find_next('p', {'data-testid': 'product-card::price'}).text
        return [single_price]

    product_page_link = BASE_URL + product_page['href']

    print(product_page_link)

    product_page_content = requests.get(product_page_link)
    soup = BeautifulSoup(product_page_content.content, "html.parser")

    # find the script tag with id __NEXT_DATA__
    next_script = soup.find('script', {'id': '__NEXT_DATA__'})

    # extract the product number from the script
    product_number = next_script.text.split('"id":"product_api_')[1].split('"')[0]

    # Call the price history API from zoom
    price_history_url = f'https://api-v1.zoom.com.br/restql/run-query/sherlock/product_price_history/1?tenant=DEFAULT&product_id={product_number}&period=days'
    response = requests.get(price_history_url)
    price_history = response.json()['product_price_history']['result']
    for tick in price_history:
        del tick['prodId']
    return price_history