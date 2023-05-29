
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='ce9e82b94bf34a399d15d54469687ee8')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='INDIA',
                                          category='business',
                                          language='en')


dt = top_headlines['articles']

for x,y in enumerate(dt):
    print(f'{x}{y["description"]}')

