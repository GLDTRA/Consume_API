from flask_restful import Resource, reqparse
from models.login import LoginModel
from providers.hash import verificar_hash, gerar_hash
from providers.token import criar_acess_token, verificar_acess_token


atributos = reqparse.RequestParser()
atributos.add_argument(
    "email",
    type=str,
    required=True,
    help="The field 'email' cannot be left blank",
)
atributos.add_argument(
    "senha",
    type=str,
    required=True,
    help="The field 'senha' cannot be left blank",
)


class Login(Resource):
    def get(self, id):
        login = LoginModel.find_id(id)
        if login:
            return login.json()
        return {"message": "email not found"}, 404

    def delete(self, id):
        login = LoginModel.find_id(id)
        if login:
            login.delete_login()
            return {"message": "usuário deleted!"}
        return {"message": "User not found"}, 404


class LoginRegister(Resource):
    def post(self):
        dados: LoginModel = atributos.parse_args()
        dados.senha = gerar_hash(dados.senha)
        if LoginModel.find_login(dados["email"]):
            return {"message": "The email {} already exists".format(dados["email"])}
        user = LoginModel(**dados)
        user.save_login()
        return {"message": "User create sucessfully", "user created": dados}, 201
