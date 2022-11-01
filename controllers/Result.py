from repositories.Result import RepResult
from models.Result import Result


class ResultController:
    def __init__(self):
        self.result_rep = RepResult()

    def index(self):
        return self.result_rep.findAll()

    def create(self, data):
        new_result = Result(data)
        return self.result_rep.save(new_result)

    def show(self, _id):
        result = Result(self.result_rep.findById(_id))
        return result.__dict__

    def update(self, _id, result):
        current = Result(self.result_rep.findById(_id))
        current.candidate_id = result["candidate_id"]
        current.table_id = result["table_id"]
        current.vote_count = result["vote_count"]
        return self.result_rep.save(current)

    def delete(self, _id):
        return self.result_rep.delete(_id)
