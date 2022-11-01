from repositories.Table import RepTable
from models.Table import Table


class TableController:
    def __init__(self):
        self.table_rep = RepTable()

    def index(self):
        return self.table_rep.findAll()

    def create(self, data):
        new_table = Table(data)
        return self.table_rep.save(new_table)

    def show(self, _id):
        table = Table(self.table_rep.findById(_id))
        return table.__dict__

    def update(self, _id, table):
        current = Table(self.table_rep.findById(_id))
        current.table_number = table["table_number"]
        current.signed_docs = table["signed_docs"]
        return self.table_rep.save(current)

    def delete(self, _id):
        return self.table_rep.delete(_id)