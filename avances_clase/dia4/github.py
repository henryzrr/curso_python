import requests
from pprint import pprint

url = 'https://api.github.com/user'
r = requests.get(url , auth=('henryzrr', '79344502henry'))
pprint(r.status_code)
pprint(r.json())