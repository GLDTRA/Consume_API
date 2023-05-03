from flask import Flask
from flask_restful import Api
from service.user import Users, User
from service.login import Login, LoginRegister, UserLogin
from service.user_credit_card import (
    GetUsersCreditCards,
    UserCreditCard,
    UsersCreditCards,
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)


@app.before_request
def cria_banco():
    banco.create_all()


api.add_resource(Users, "/users")
api.add_resource(User, "/user/<int:id>")
api.add_resource(Login, "/login/<int:id>")
api.add_resource(LoginRegister, "/login-register")
api.add_resource(UserLogin, "/user-login")
api.add_resource(GetUsersCreditCards, "/get-users-credit-cards")
api.add_resource(UserCreditCard, "/user-credit-card/<string:id>")
api.add_resource(UsersCreditCards, "/users-credit-cards")

if __name__ == "__main__":
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)
