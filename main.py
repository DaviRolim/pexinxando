# import both scraper files
import pelando_scraper
import buscape_scraper
from time import sleep
import math

# products_with_good_offers_pelando = pelando_scraper.scrape()
products_with_good_offers_pelando = [{"name":"Baseus 20000mah Power Bank Pd Qc 20w",
                                       "offer_price":"152",
                                       "temperature":"612",
                                       "seller":"AliExpress"}]
for offer in products_with_good_offers_pelando:
    print(offer['name'])
    product_price_history = buscape_scraper.scrape(offer['name'])
    offer['price_history'] = product_price_history

    if len(product_price_history) > 1:
        lowest_price = min(product_price_history, key=lambda x: x['price'])
        offer['lowest_price'] = lowest_price['price']
        offer['lowest_price_date'] = lowest_price['date']

        avg_price = sum([x['price'] for x in product_price_history]) / len(product_price_history)
        offer['avg_price'] = avg_price
        offer['current_price'] = product_price_history[-1]['price']
    elif (len(product_price_history) == 1):
        offer['lowest_price'] = product_price_history[0]
        offer['avg_price'] = product_price_history[0]
        offer['current_price'] = product_price_history[0]
    

    if len(product_price_history) > 0:
        # parse current price to float IF is not a float already: example of current price: R$ 1.999,00
        if type(offer['current_price']) is str:
            offer['current_price'] = offer['current_price'].replace('R$ ', '').replace('.', '').replace(',', '.')

        
        # calculate percentage difference from offer['offer_price'] and offer['current_price']
        difference = float(offer['offer_price']) - float(offer['current_price'])
        ratio2 = (float(offer['offer_price']) + float(offer['current_price'])) / 2
        percentage_difference = (difference / ratio2) * 100
        offer['discount'] = str(abs(math.floor(percentage_difference))) + '%'
    
    # sleep(2)
    

# product_price_history = buscape_scraper.scrape('The Frame 50')
# print(product_price_history)
print(products_with_good_offers_pelando)

