from sql_alchemy import banco


class LoginModel(banco.Model):
    __tablename__ = "login"

    id = banco.Column(banco.Integer, primary_key=True)
    email = banco.Column(banco.String(70), nullable=False)
    senha = banco.Column(banco.String(50), nullable=False)

    def __init__(self, email, senha) -> None:
        self.email = email
        self.senha = senha

    def json(self):
        return {"id": self.id, "email": self.email}

    @classmethod
    def find_id(cls, id):
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None

    @classmethod
    def find_login(cls, email):
        user_login = cls.query.filter_by(email=email).first()
        if user_login:
            return user_login
        return None

    def save_login(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_login(self):
        banco.session.delete(self)
        banco.session.commit()
