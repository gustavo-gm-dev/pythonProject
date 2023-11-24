import requests
import json
from elasticsearch import Elasticsearch

client = Elasticsearch(
    ['https://elk-motor-oc-dev.ovd.com.br'],
    basic_auth=('elastic', 'G6U2j01xr70942e4pqAFqPlR')
)


url = "https://elk-motor-oc-dev.ovd.com.br/produtos/_search/template"

payload = json.dumps({
  "params": {
    "ultimo_valor": 0,
    "qtde_registros": 1
  },
  "id": "qry_batimento_precos"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZWxhc3RpYzpHNlUyajAxeHI3MDk0MmU0cHFBRnFQbFI=',
  'Cookie': 'eef0dbf09e590d04f8df822bb51c08c8=688d67b19d8112b4fddb503c6bc13cfa'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
