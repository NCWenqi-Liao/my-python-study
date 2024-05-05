# import requests
# from lxml import etree
# index = 'https://tieba.baidu.com/p/8613990813'
# r = requests.get(index).text
# selector = etree.HTML(r)
# image_urls = selector.xpath('//img[@class="BDE_Image"]/@src')
# for image_url in image_urls:
#     print(image_url)


import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(data)
print(json_string)

import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)

import json

# with open('stations_json.txt', 'r',encoding='utf-8') as file:
#     data = json.load(file)
#     print(data)


