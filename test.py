import requests

api_item_list = requests.get('https://fakestoreapi.com/products?limit=10').json()

print(api_item_list)