from models.Table import TableModel as Table
import database as db

database = db.db_connection()


class TableController:
    def __init__(self):
        pass

    @staticmethod
    def index():
        tables = database['tables']
        tables_received = tables.find()
        return list(tables_received)

    @staticmethod
    def get_by_table(table_number):
        tables = database['tables']
        search_criteria = {"table_number": int(table_number)}

        if tables.find_one(search_criteria) is None:
            return {"status": "failed", "message": "la mesa " + str(table_number) + " no existe"}

        table = tables.find_one(search_criteria)
        return table

    @staticmethod
    def create(data):
        tables = database['tables']

        table_number = data["table_number"]
        signed_docs = data["signed_docs"]

        table = Table(table_number, signed_docs)
        tables.insert_one(table.to_db_collection())

        return {
            "status": "ok",
            "table_number": table_number,
            "signed_docs": signed_docs
        }

    @staticmethod
    def delete(table_number):
        tables = database['tables']

        if tables.find_one({"table_number": table_number}) is None:
            return {"status": "failed", "message": "la mesa " + str(table_number) + " no existe"}

        tables.delete_one({"table_number": table_number})
        return {"status": "deleted", "table_number": table_number}

    @staticmethod
    def edit(table_number, signed_docs):
        tables = database['tables']
        search_criteria = {"table_number": table_number}

        if tables.find_one(search_criteria) is None:
            return {"status": "failed", "message": "la mesa " + str(table_number) + " no existe"}

        tables.update_one(search_criteria, {'$set': {"table_number": table_number, "signed_docs": signed_docs}})

        return {
            "status": "ok",
            "message": "la mesa " + str(table_number) + " ha sido actualizada",
            "table_number": table_number,
            "signed_docs": signed_docs
        }
