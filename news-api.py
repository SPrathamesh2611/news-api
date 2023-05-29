
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='YOUR-API-KEY')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='INDIA',
                                          category='business',
                                          language='en')


dt = top_headlines['articles']

for x,y in enumerate(dt):
    print(f'{x}{y["description"]}')

