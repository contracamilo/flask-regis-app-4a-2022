from models.Table import TableModel
from flask import jsonify


class TableController:
    def __init__(self):
        pass

    @staticmethod
    def index():
        print("creating controller")
        table = {
            "number": 3,
            "signed_documents": 390
        }
        return [table]

    @staticmethod
    def create(self, data):
        print("create table")
        new_student = TableModel(data)
        return new_student.__dict__

    @staticmethod
    def get_by_id(self, idx, data):
        print("Get Table by id ", id)
        table = {
            "number": id,
            "signed_documents": 390
        }
        return table

    @staticmethod
    def update(self, idx, data):
        print("update table" + idx)
        table = TableModel(data)
        return table.__dict__

    @staticmethod
    def delete(self, idx):
        print("Delete by id ", idx)
        return {"deleted_count": 1}
