from models.AbstractModel import AbstractModel


class TableModel:
    def __init__(self, table_number, signed_docs):
        self.table_number = table_number
        self.signed_docs = signed_docs

    def to_db_collection(self):
        print(self)
        return {'table_number': self.table_number, 'signed_docs': self.signed_docs}
