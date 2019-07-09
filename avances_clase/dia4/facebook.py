import requests
from pprint import pprint

token='EAAjxI6QIyu4BAIgPyIZBmH9foZBvpzOb2dshp4yKaglZAcmKcb9FGqzn9uaRHIP2LCTauXPyGUaX2UqZC76b8JDGAbPTnHr5DWVrisJiTd1uz1pdAQFahlrvINGSQJkclL4nylNyupdTUnCtXZAv7QanXk0zZA1hwhVP9FLDgkFvpZBRWK0HGJp0zxC58kia3SpkVM4g78F5gZDZD'
url='https://graph.facebook.com/v3.2/me?access_token='+token

r = requests.get(url)
pprint(r.json())