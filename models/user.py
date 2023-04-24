from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()


class UserModel(database.Model):
    __tablename__ = "user"

    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(50))
    email = database.Column(database.String(70))

    def __init__(self, id, nome, email) -> None:
        self.id = id
        self.nome = nome
        self.email = email

    def json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}

    @classmethod
    def find_user(cls, id):
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None

    def save_user(self):
        database.session.add(self)
        database.session.commit()

    def update_user(self, nome, email):
        self.nome = nome
        self.email = email

    def delete_user(self):
        database.session.delete(self)
        database.session.commit()
