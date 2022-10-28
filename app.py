from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import json
from waitress import serve
from controllers.Table import TableController

app = Flask(__name__)
cors = CORS(app)


def load_config_file():
    with open('config.json') as file:
        data = json.load(file)
    return data

'''
**** CRUD mesas de votacion ****
'''

@app.route("/mesas", methods=['GET', 'POST'])
def get_create_tables():
    table = TableController.index()
    all_tables = json.dumps(table, default=str)

    if request.method == 'POST':
        new_table = json.loads(request.data)

        if new_table["table_number"] and new_table["signed_docs"]:
            table = TableController.create(data=new_table)
        return jsonify(table)

    return json.loads(all_tables)


@app.route("/mesas/<table_number>", methods=['GET'])
def get_table_by_number(table_number):
    table = TableController.get_by_table(table_number)
    table = json.dumps(table, default=str)
    return json.loads(table)


@app.route("/mesas/borrar", methods=['DELETE'])
def delete_tables():
    deleted_table = json.loads(request.data)
    table = TableController.delete(deleted_table["table_number"])
    return jsonify(table)


@app.route("/mesas/editar", methods=['PUT'])
def edit_tables():
    edited_table = json.loads(request.data)
    table_number = edited_table["table_number"]
    signed_docs = edited_table["signed_docs"]

    table = TableController.edit(table_number, signed_docs)
    return jsonify(table)


if __name__ == '__main__':
    dataConfig = load_config_file()
    url = dataConfig["backendURL"]
    port = dataConfig["port"]

    print("running at: " + "http://" + url + ":" + str(port))
    serve(app, host=url, port=port)
