from flask import Flask
from flask import jsonify
from flask import request
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


@app.route('/', methods=["GET"])
def test():
    response = {
        "user": "camilo"
    }
    return jsonify(response)


@app.route("/mesas", methods=['GET'])
def get_tables():
    table = TableController.index()
    return jsonify(table)



'''
@app.route("/estudiantes/<string:id>", methods=['DELETE'])
def eliminarEstudiante(id):
    json = miControladorEstudiante.delete(id)
    return jsonify(json)
'''

if __name__ == '__main__':
    dataConfig = load_config_file()
    url = dataConfig["backendURL"]
    port = dataConfig["port"]

    print("running at: " + "http://" + url + ":" + str(port))
    serve(app, host=url, port=port)
