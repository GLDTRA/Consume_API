from flask_restful import Resource, reqparse
from models.user import UserModel


class Users(Resource):
    def get(self):
        return {"users": [user.json() for user in UserModel.query.all()]}


class User(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome")
    argumentos.add_argument(
        "email", type=str, required=True, help="The field 'email' cannot be null!"
    )

    def get(self, id):
        user = UserModel.find_user(id)
        if user:
            return user.json()
        return {"message": "user not found"}, 404

    def post(self, id):
        if UserModel.find_user(id):
            return {"message": "User id '{}' already exist".format(id)}, 400

        dados = User.argumentos.parse_args()
        user = UserModel(id, **dados)
        try:
            user.save_user()
        except:
            return {"message": "An internal error ocorred trying to save user"}, 500
        return user.json()

    def put(self, id):
        dados = User.argumentos.parse_args()
        user_encontrado = UserModel.find_user(id)
        if user_encontrado:
            user_encontrado.update_user(**dados)
            try:
                UserModel.save_user(user_encontrado)
            except:
                return {"message": "An internal error ocorred trying to save user"}, 500
            return user_encontrado.json(), 200
        return {"message": "user id '{}' not found".format(id)}

    def delete(self, id):
        user = UserModel.find_user(id)
        if user:
            user.delete_user()
            return {"message": "usuário deleted!"}
        return {"message": "User not found"}, 404
