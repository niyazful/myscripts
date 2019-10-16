import requests

URL        = "https://website.ru/api'
PAYLOAD ={}
domain_list = open("domains.list", mode="r")

for domain in domain_list:
    PAYLOAD['ident']  = "id"
    PAYLOAD['white'] = domain

    r = requests.post(url=URL, json=PAYLOAD)
    result = r.json()
