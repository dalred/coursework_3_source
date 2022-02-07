from project.dao.models.director import Director
from project.exceptions import ItemNotFound


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        director = self.session.query(Director).get(bid)
        if not director:
            raise ItemNotFound("Не найден Director!")
        else:
            return director

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, update):
        self.session.add(update)
        self.session.commit()
