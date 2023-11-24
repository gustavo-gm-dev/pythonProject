import requests
import json
from elasticsearch import Elasticsearch

client = Elasticsearch(
    [''],
    basic_auth=('', '')
)


url = ""

payload = json.dumps({
  "params": {
    "ultimo_valor": 0,
    "qtde_registros": 1
  },
  "id": "qry_batimento_precos"
})
headers = {
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
