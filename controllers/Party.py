from repositories.Party import RepParty
from models.Party import Party


class PartyController:
    def __init__(self):
        self.party_rep = RepParty()

    def index(self):
        return self.party_rep.findAll()

    def create(self, data):
        new_party = Party(data)
        return self.party_rep.save(new_party)

    def show(self, _id):
        party = Party(self.party_rep.findById(_id))
        return party.__dict__

    def update(self, _id, party):
        current = Party(self.party_rep.findById(_id))
        current.party_name = party["party_name"]
        current.motto = party["motto"]
        return self.party_rep.save(current)

    def delete(self, _id):
        return self.party_rep.delete(_id)
