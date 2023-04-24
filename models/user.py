from sql_alchemy import banco


class UserModel(banco.Model):
    __tablename__ = "user"

    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(50))
    email = banco.Column(banco.String(70))

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
        banco.session.add(self)
        banco.session.commit()

    def update_user(self, nome, email):
        self.nome = nome
        self.email = email

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()
