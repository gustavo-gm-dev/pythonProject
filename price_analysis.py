import datetime
import json
import sys
import csv

import requests
import logging


data_atual = datetime.datetime.now()
data_sem_caracteres = data_atual.strftime("%Y%m%d%H%M%S")

filename_log = "logs/log_" + data_sem_caracteres

logging.basicConfig(filename=filename_log, level=logging.INFO,
                    format="%(asctime)s: %(levelname)s: %(message)s")


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
            logging.error("Error: Endpoint must be a string.")
            sys.exit()

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, set_username):
        if isinstance(set_username, str):
            self._username = set_username
        else:
            logging.error("Error: Username must be a string.")
            sys.exit()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, set_password):
        if isinstance(set_password, str):
            self._password = set_password
        else:
            logging.error("Error: Password must be a string.")
            sys.exit()

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, set_directory):
        if isinstance(set_directory, str):
            self._directory = set_directory
        else:
            logging.error("Error: Directory must be a string.")
            sys.exit()

    @property
    def number_records(self):
        return self._number_records

    @number_records.setter
    def number_records(self, set_number_records):
        if isinstance(set_number_records, int):
            self._number_records = set_number_records
        else:
            logging.error("Error: The number_records must be an integer value.")
            sys.exit()

    @property
    def last_record(self):
        return self._last_record

    @last_record.setter
    def last_record(self, set_last_record):
        if isinstance(set_last_record, int):
            self._last_record = set_last_record
        else:
            logging.error("Error: The last_record must be an integer value.")

    @property
    def json_response(self):
        return self._json_response

    @json_response.setter
    def json_response(self, set_json_response):
        if isinstance(set_json_response, dict):
            self._json_response = set_json_response
        else:
            logging.error("Error: Json")


def call_api(variables):
    url = variables.endpoint + "/produtos/_search/template"

    payload = json.dumps({
        "params": {
            "ultimo_valor": variables.last_record,
            "qtde_registros": variables.number_records
        },
        "id": "qry_batimento_precos"
    })

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("GET", url, auth=(variables.username, variables.password),
                                    headers=headers, data=payload)
        response.raise_for_status()

        return response

    except requests.exceptions.HTTPError as e:
        logging.error("Error HTTP: {}".format(e.response.status_code))
        logging.error("Error service:", e.response.text)
        return None

    except requests.exceptions.RequestException as e:
        logging.error("Error requisition: {}".format(e))
        return None
        # with open("json_example.txt", "r") as f:
        #     data = json.load(f)
        # return data


def parse_data(json_data):

    id_value = None

    # Executa um parsing no Json
    for hits in json_data["hits"]["hits"]:
        id_value = hits["_id"]
        for inner_hits in hits["inner_hits"]["listasPrecos.precos"]["hits"]["hits"]:
            writer.writerow([
                id_value,
                inner_hits["_source"]["preco"],
                inner_hits["_source"]["uf"],
                inner_hits["_source"]["fimVigencia"],
                inner_hits["_source"]["inicioVigencia"],
                inner_hits["_source"]["tipoPreco"],
                inner_hits["_source"]["listaPreco"]
            ])
    return int(id_value)


def valid_variables(variables):
    if variables is not None or variables != "":
        if variables.endpoint is None:
            logging.error("Endpoint not defined")
            sys.exit()

        elif variables.username is None:
            logging.error("Username not defined")
            sys.exit()

        elif variables.password is None:
            logging.error("Password not defined")
            sys.exit()

        elif variables.directory is None:
            logging.error("Directory not defined")
            sys.exit()

        elif variables.number_records is None:
            variables.number_records = 5000
            logging.info("Registration quantity per query not defined. Default: " + str(variables.number_records))

        elif variables.last_record is None:
            variables.last_record = 0
            logging.info("Last record processed unidentified. Default: " + str(variables.last_record))


if __name__ == "__main__":
    logging.info("The program has started.")
    # Chama colecao das variaveis
    variables = InputVariables()

    if len(sys.argv[1:]) == 6:
        #Intruções python price_analysis.py endpoint user pass qt_registro diretorio_destino
        variables.endpoint = sys.argv[1]
        variables.username = sys.argv[2]
        variables.password = sys.argv[3]
        variables.directory = sys.argv[4]
        variables.number_records = int(sys.argv[5])
        variables.last_record = int(sys.argv[6])
    else:
        # logging.error('Not all input variables were defined')
        # sys.exit()
        variables.endpoint = "endpoint"
        variables.username = "user"
        variables.password = "pass"
        variables.directory = "dir"
        variables.number_records = 10000
        variables.last_record = 0

    #Valida variaveis de entrada
    valid_variables(variables)

    #Variavel que será utilizada caso uma chamada api de erro 500 timeout
    resend = 0

    #Varivel para garantir que não ira efetuar a mesma chamada
    last_register = None

    #Variavel de diretorio
    file_csv = variables.directory + "/price_analysis_"

    # Cria um escritor CSV.
    with open(file_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(["id_produto", "preco", "uf", "fimVigencia", "inicioVigencia", "tipoPreco", "listaPreco"])

        while variables.last_record is not None:

            if variables.last_record != last_register:
                last_register = variables.last_record
            else:
                logging.error('Error: Lopping, last register: {}'.format(str(last_register)))
                sys.exit()

            # Efetua chamada para API com as variaveis
            api_response = call_api(variables)

            if api_response is not None:
                if api_response.status_code == 200:
                    resend = 0 #Declara variavel novamente para 0
                    logging.info("API callback: " + str(api_response))
                elif api_response.status_code == 500 and resend < 1:
                    logging.error("Error: Timeout response API, resending")
                    resend = 1
                    number_rescords_origin = variables.number_records
                    variables.number_records = variables.number_records // 2
                    # Chama novamente com metade dos registro em caso de erro
                    api_response = call_api(variables)
                elif api_response.status_code == 404:
                    logging.error("Error 404: Resource not found.")
                    sys.exit()
                else:
                    logging.error("General Error")
                    sys.exit()

            variables.last_record = parse_data(api_response.text)
            # variables.last_record = parse_data(api_response)

    logging.info("The program has been completed.")
