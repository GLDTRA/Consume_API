from flask_restful import Resource, reqparse
from models.user_credit_card import UserCreditCardModel
from providers.hash import gerar_hash
import requests
from sql_alchemy import banco


class UsersCreditCards(Resource):
    def get(self):
        return {"users": [user.json() for user in UserCreditCardModel.query.all()]}


class UserCreditCard(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("avatar")
    argumentos.add_argument("user_name", type=str, required=True)
    argumentos.add_argument("color_favorito", type=str, required=True)
    argumentos.add_argument("foto_dni", type=str, required=True)
    argumentos.add_argument("auto", type=str, required=True)
    argumentos.add_argument("auto_modelo", type=str, required=True)
    argumentos.add_argument("auto_tipo", type=str, required=True)
    argumentos.add_argument("auto_color", type=str, required=True)

    def get(self, id):
        user_credit_card: UserCreditCardModel = UserCreditCardModel.find_user_card(id)
        if user_credit_card:
            return user_credit_card
        return {"message": "user not found"}, 404


class GetUsersCreditCards(Resource):
    def get(self):
        response = requests.get(
            "https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios"
        )
        if response.status_code == 200:
            data = response.json()
        else:
            return "Falha na solicitação. Código de status: {}".format(
                response.status_code
            )

        for item in data:
            novo_item: object = UserCreditCardModel(
                id=item["id"],
                fec_alta=item["fec_alta"],
                user_name=item["user_name"],
                codigo_zip=item["codigo_zip"],
                credit_card_num=item["credit_card_num"],
                credit_card_ccv=item["credit_card_ccv"],
                cuenta_numero=item["cuenta_numero"],
                direccion=item["direccion"],
                geo_latitud=item["geo_latitud"],
                geo_longitud=item["geo_longitud"],
                color_favorito=item["color_favorito"],
                foto_dni=item["foto_dni"],
                ip=item["ip"],
                auto=item["auto"],
                auto_modelo=item["auto_modelo"],
                auto_tipo=item["auto_tipo"],
                auto_color=item["auto_color"],
                cantidad_compras_realizadas=item["cantidad_compras_realizadas"],
                avatar=item["avatar"],
                fec_birthday=item["fec_birthday"],
            )
            novo_item.fec_alta = gerar_hash(novo_item.fec_alta)
            novo_item.codigo_zip = gerar_hash(novo_item.codigo_zip)
            novo_item.credit_card_num = gerar_hash(novo_item.credit_card_num)
            novo_item.credit_card_ccv = gerar_hash(novo_item.credit_card_ccv)
            novo_item.cuenta_numero = gerar_hash(novo_item.cuenta_numero)
            novo_item.direccion = gerar_hash(novo_item.direccion)
            novo_item.geo_latitud = gerar_hash(novo_item.geo_latitud)
            novo_item.geo_longitud = gerar_hash(novo_item.geo_longitud)
            novo_item.ip = gerar_hash(novo_item.ip)
            novo_item.cantidad_compras_realizadas = gerar_hash(
                str(novo_item.cantidad_compras_realizadas)
            )
            banco.session.add(novo_item)
        banco.session.commit()
        banco.session.close()

        return "Dados da API salvos com sucesso no banco de dados!"
