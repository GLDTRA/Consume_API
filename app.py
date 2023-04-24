from flask import Flask
from flask_restful import Api, Resource
from service.user import Users, User
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)


@app.before_first_request
def cria_banco():
    database.create_all()


api.add_resource(Users, "/users")

api.add_resource(User, "/user/<int:id>")

if __name__ == "__main__":
    from flask_sqlalchemy import SQLAlchemy

    database = SQLAlchemy()

    database.init_app(app)
    app.run(debug=True)
