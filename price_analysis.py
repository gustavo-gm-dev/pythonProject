import json
import sys

from pandas import json_normalize
import requests


class InputVariables:
    def __init__(self):
        self._endpoint = None
        self._username = None
        self._password = None
        self._directory = None
        self._number_records = None
        self._last_record = None
        self._json_response = None

    @property
    def endpoint(self):
        return self._endpoint

    @endpoint.setter
    def endpoint(self, set_endpoint):
        if isinstance(set_endpoint, str):
            self._endpoint = set_endpoint
        else:
            print("Error: Endpoint must be a string.")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, set_username):
        if isinstance(set_username, str):
            self._username = set_username
        else:
            print("Error: Username must be a string.")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, set_password):
        if isinstance(set_password, str):
            self._password = set_password
        else:
            print("Error: Password must be a string.")

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, set_directory):
        if isinstance(set_directory, str):
            self._directory = set_directory
        else:
            print("Error: Directory must be a string.")

    @property
    def number_records(self):
        return self._number_records

    @number_records.setter
    def number_records(self, set_number_records):
        if isinstance(set_number_records, int):
            self._number_records = set_number_records
        else:
            print("Error: The number_records must be an integer value.")

    @property
    def last_record(self):
        return self._last_record

    @last_record.setter
    def last_record(self, set_last_record):
        if isinstance(set_last_record, int):
            self._last_record = set_last_record
        else:
            print("Error: The last_record must be an integer value.")

    @property
    def json_response(self):
        return self._json_response

    @json_response.setter
    def json_response(self, set_json_response):
        if isinstance(set_json_response, dict):
            self._json_response = set_json_response
        else:
            print("Error: Json")


def call_api(variables):
    url = variables.endpoint + "/produtos/_search/template"

    payload = json.dumps({
        "params": {
            "ultimo_valor": 0,
            "qtde_registros": 1
        },
        "id": "qry_batimento_precos"
    })

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("GET", url, auth=(variables.username, variables.password), headers=headers, data=payload)
        print(response.text)

        response.raise_for_status()
        return response

    except requests.exceptions.HTTPError as e:
        print("Error HTTP: {}".format(e.response.status_code))
        print("Erro do servidor:", e.response.text)
        return None

    except requests.exceptions.RequestException as e:
        print("Error na requisicao: {}".fotmat(e))
        return None

def parse_data(json_data):
    # Carrega o JSON

    #df = pd.read_json(json_data)
    df = json_normalize(json_data, "_source")

    print(df)

if __name__ == "__main__":
    # Chama colecao das variaveis
    variables = InputVariables()

    variables.endpoint = ""
    variables.username = ""
    variables.password = ""
    variables.directory = "C:/Users/ovd8439/Documents/Analista_Documentacao/36 - ElasticSearch"
    variables.number_records = 10
    variables.last_record = 0

    resend = 0

    # Efetua chamada para API com as variaveis
    api_response = call_api(variables)

    if api_response is not None:
        if api_response.status_code == 200:
            resend = 0
            print(api_response)
        elif api_response.status_code == 500 and resend < 1:
            print("Error: Timeout response API, efetuando reenvio")
            resend = 1
            number_rescords_origin = variables.number_records
            variables.number_records = variables.number_records // 2
            # Chama novamente com metade dos registro em caso de erro
            api_response = call_api(variables)
        elif api_response.status_code == 404:
            print("Erro 404: Recurso nao encontrado.")
            sys.exit()
        else:
            print("General Error")
            sys.exit()

    print(api_response.text)
    parse_data(api_response.text)
