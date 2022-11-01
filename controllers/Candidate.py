from repositories.Candidate import RepCandidate
from models.Candidate import Candidate


class CandidateController:
    def __init__(self):
        self.candidate_rep = RepCandidate()

    def index(self):
        return self.candidate_rep.findAll()

    def create(self, data):
        new_candidate = Candidate(data)
        return self.candidate_rep.save(new_candidate)

    def show(self, _id):
        candidate = Candidate(self.candidate_rep.findById(_id))
        return candidate.__dict__

    def update(self, _id, candidate):
        current = Candidate(self.candidate_rep.findById(_id))
        current.resolution_number = candidate["resolution_number"]
        current.name = candidate["name"]
        current.surname = candidate["surname"]
        current.document_id = candidate["document_id"]
        current.party_id = candidate["party_id"]
        return self.candidate_rep.save(current)

    def delete(self, _id):
        return self.candidate_rep.delete(_id)
