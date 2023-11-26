import json
import csv
import sys

print(sys.argv[1])
print(sys.argv[2])

with open("json_example.txt", "r") as f:
    data = json.load(f)

 # Cria um escritor CSV.
with open("output_file.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(["id_produto", "preco", "uf", "fimVigencia", "margemDescPadrao", "inicioVigencia", "desconto", "tipoPreco", "etiquetas", "listaPreco", "precoOriginal", "margemDescTotal" ])

    for hits in data["hits"]["hits"]:
        id_value = hits["_id"]
        for inner_hits in hits["inner_hits"]["listasPrecos.precos"]["hits"]["hits"]:
            writer.writerow([
                id_value,
                inner_hits["_source"]["preco"],
                inner_hits["_source"]["uf"],
                inner_hits["_source"]["fimVigencia"],
                inner_hits["_source"]["margemDescPadrao"],
                inner_hits["_source"]["inicioVigencia"],
                inner_hits["_source"]["desconto"],
                inner_hits["_source"]["tipoPreco"],
                inner_hits["_source"]["listaPreco"],
                inner_hits["_source"]["precoOriginal"],
                inner_hits["_source"]["margemDescTotal"]
            ])
    # print(id_value)
    # print(inner_hits["_source"]["preco"])
    # print(inner_hits["_source"]["uf"])
    # print(inner_hits["_source"]["fimVigencia"])
    # print(inner_hits["_source"]["margemDescPadrao"])
    # print(inner_hits["_source"]["inicioVigencia"])
    # print(inner_hits["_source"]["desconto"])
    # print(inner_hits["_source"]["tipoPreco"])
    # print(inner_hits["_source"]["etiquetas"])
    # print(inner_hits["_source"]["listaPreco"])
    # print(inner_hits["_source"]["precoOriginal"])
    # print(inner_hits["_source"]["margemDescTotal"])

