from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import json
from waitress import serve
from controllers.Table import TableController
from controllers.Party import PartyController
from controllers.Candidate import CandidateController
from controllers.Result import ResultController

app = Flask(__name__)
cors = CORS(app)


def load_config_file():
    with open('config.json') as file:
        data = json.load(file)
    return data


partyController = PartyController()
tableController = TableController()
candidateController = CandidateController()
resultController = ResultController()

'''
**** CRUD mesas de votacion ****
'''


@app.route("/mesas", methods=['GET'])
def get_tables():
    data = tableController.index()
    return jsonify(data)


@app.route("/mesas", methods=['POST'])
def create_table():
    data = request.get_json()
    new_table = tableController.create(data=data)
    return jsonify(new_table)


@app.route("/mesas/<string:_id>", methods=['GET'])
def get_table_by_id(_id):
    data = tableController.show(_id)
    return jsonify(data)


@app.route("/mesas/<string:_id>", methods=['PUT'])
def update_table(_id):
    data = request.get_json()
    updated_table = tableController.update(_id, data)
    return jsonify(updated_table)


@app.route("/mesas/<string:_id>", methods=['DELETE'])
def delete_table(_id):
    deleted_party = tableController.delete(_id)
    return jsonify(deleted_party)


'''
**** CRUD partidos ****
'''


@app.route("/partidos", methods=['GET'])
def get_parties():
    data = partyController.index()
    return jsonify(data)


@app.route("/partidos", methods=['POST'])
def create_party():
    data = request.get_json()
    new_party = partyController.create(data=data)
    return jsonify(new_party)


@app.route("/partidos/<string:_id>", methods=['GET'])
def get_party_by_id(_id):
    data = partyController.show(_id)
    return jsonify(data)


@app.route("/partidos/<string:_id>", methods=['PUT'])
def update_party(_id):
    data = request.get_json()
    updated_party = partyController.update(_id, data)
    return jsonify(updated_party)


@app.route("/partidos/<string:_id>", methods=['DELETE'])
def delete_party(_id):
    deleted_party = partyController.delete(_id)
    return jsonify(deleted_party)


'''
**** CRUD candidatos ****
'''


@app.route("/candidatos", methods=['GET'])
def get_candidates():
    data = candidateController.index()
    return jsonify(data)


@app.route("/candidatos", methods=['POST'])
def create_candidate():
    data = request.get_json()
    new_candidate = candidateController.create(data=data)
    return jsonify(new_candidate)


@app.route("/candidatos/<string:_id>", methods=['GET'])
def get_candidate_by_id(_id):
    data = candidateController.show(_id)
    return jsonify(data)


@app.route("/candidatos/<string:_id>", methods=['PUT'])
def update_candidate(_id):
    data = request.get_json()
    updated_candidate = candidateController.update(_id, data)
    return jsonify(updated_candidate)


@app.route("/candidatos/<string:_id>", methods=['DELETE'])
def delete_cadidate(_id):
    deleted_candidate = candidateController.delete(_id)
    return jsonify(deleted_candidate)


'''
**** CRUD Resultados ****
'''


@app.route("/resultados", methods=['GET'])
def get_result():
    data = resultController.index()
    return jsonify(data)


@app.route("/resultados", methods=['POST'])
def create_result():
    data = request.get_json()
    new_result = resultController.create(data=data)
    return jsonify(new_result)


@app.route("/resultados/<string:_id>", methods=['GET'])
def get_result_by_id(_id):
    data = resultController.show(_id)
    return jsonify(data)


@app.route("/resultados/<string:_id>", methods=['PUT'])
def update_result(_id):
    data = request.get_json()
    updated_result = resultController.update(_id, data)
    return jsonify(updated_result)


@app.route("/resultados/<string:_id>", methods=['DELETE'])
def delete_result(_id):
    deleted_result = resultController.delete(_id)
    return jsonify(deleted_result)


if __name__ == '__main__':
    dataConfig = load_config_file()
    url = dataConfig["backendURL"]
    port = dataConfig["port"]

    print("running at: " + "http://" + url + ":" + str(port))
    serve(app, host=url, port=port)
