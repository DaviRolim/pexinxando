# Example of how to run the api
python flask_api.py  

Then send a request `curl http://localhost:5000/api/v1/search?search_term=The+Frame+50`

## Example response
```json
response {
  buscape: {
    lowest_price: 2799.99,
    lowest_price_date: '2022-12-27',
    avg_price: 3384.4950000000003,
    current_price: 3199.99
  },
  amazon: [
    {
      title: 'Smart TV QLED 50" 4K UHD Samsung QN50LS03B - The Frame, Wifi',
      price: '3.309,99',
      stars: '5,0 de 5 estrelas',
      number_of_reviews: '(6)',
      link: 'https://www.amazon.com.br/Smart-QLED-UHD-Samsung-QN50LS03B/dp/B0B4V7CCW3/ref=sr_1_1?keywords=The+Frame+50&qid=1675181977&sr=8-1&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147'
    },
    {
      title: 'Smart TV Philco 40” PTV40G65RCH Roku TV Dolby Audio Led',
      price: '1.499,01',
      stars: '4,6 de 5 estrelas',
      number_of_reviews: '(93)',
      link: 'https://www.amazon.com.br/PHILCO-Smart-PTV40G65RCH-Dolby-Audio/dp/B09X1X15F2/ref=sr_1_2?keywords=The+Frame+50&qid=1675181977&sr=8-2&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147'
    }
  ]
}
```