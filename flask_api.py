# simple flask api to call buscape_scraper and amazon_scraper and return the results as json
import json
from flask import Flask, request
from buscape_scraper import scrape as scrape_buscape
from buscape_scraper import get_price_stats
from amazon_scraper import scrape as scrape_amazon

app = Flask(__name__)

@app.route('/api/v1/search', methods=['GET'])
def search():
    search_term = request.args.get('search_term')
    if not search_term:
        return json.dumps({'error': 'search_term is required'}), 400
    buscape_results = scrape_buscape(search_term)
    stats = get_price_stats(buscape_results)
    amazon_results = scrape_amazon(search_term)
    return json.dumps({'buscape': stats, 'amazon': amazon_results})

if __name__ == "__main__":
    app.run(debug=True)
# example of how to run the api
# python flask_api.py
# curl http://localhost:5000/api/v1/search?search_term=The+Frame+50