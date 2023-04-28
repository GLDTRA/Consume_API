from sql_alchemy import banco


class UserCreditCardModel(banco.Model):
    __tablename__ = "user_credit_card"

    id = banco.Column(banco.Integer, primary_key=True)
    fec_alta = banco.Column(banco.String(255))
    user_name = banco.Column(banco.String(255))
    codigo_zip = banco.Column(banco.String(255))
    credit_card_num = banco.Column(banco.String(255))
    credit_card_ccv = banco.Column(banco.String(255))
    cuenta_numero = banco.Column(banco.String(255))
    direccion = banco.Column(banco.String(255))
    geo_latitud = banco.Column(banco.String(255))
    geo_longitud = banco.Column(banco.String(255))
    color_favorito = banco.Column(banco.String(255))
    foto_dni = banco.Column(banco.String(255))
    ip = banco.Column(banco.String(255))
    auto = banco.Column(banco.String(255))
    auto_modelo = banco.Column(banco.String(255))
    auto_tipo = banco.Column(banco.String(255))
    auto_color = banco.Column(banco.String(255))
    cantidad_compras_realizadas = banco.Column(banco.Integer)
    avatar = banco.Column(banco.String(255))
    fec_birthday = banco.Column(banco.String(255))

    def __init__(
        self,
        id,
        avatar,
        fec_alta,
        user_name,
        codigo_zip,
        credit_card_num,
        credit_card_ccv,
        cuenta_numero,
        direccion,
        geo_latitud,
        geo_longitud,
        color_favorito,
        foto_dni,
        ip,
        auto,
        auto_modelo,
        auto_tipo,
        auto_color,
        cantidad_compras_realizadas,
        fec_birthday,
    ) -> None:
        self.id = id
        self.avatar = avatar
        self.fec_alta = fec_alta
        self.user_name = user_name
        self.codigo_zip = codigo_zip
        self.credit_card_num = credit_card_num
        self.credit_card_ccv = credit_card_ccv
        self.cuenta_numero = cuenta_numero
        self.direccion = direccion
        self.geo_latitud = geo_latitud
        self.geo_longitud = geo_longitud
        self.color_favorito = color_favorito
        self.foto_dni = foto_dni
        self.ip = ip
        self.auto = auto
        self.auto_modelo = auto_modelo
        self.auto_tipo = auto_tipo
        self.auto_color = auto_color
        self.cantidad_compras_realizadas = cantidad_compras_realizadas
        self.fec_birthday = fec_birthday

    @classmethod
    def find_user_card(cls, id):
        user_credit_card: UserCreditCardModel = cls.query.filter_by(id=id).first()
        if user_credit_card:
            return user_credit_card.json()
        return None

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def json(self):
        return {
            "id": self.id,
            "avatar": self.avatar,
            "user_name": self.user_name,
            "color_favorito": self.color_favorito,
            "foto_dni": self.foto_dni,
            "auto": self.auto,
            "auto_modelo": self.auto_modelo,
            "auto_tipo": self.auto_tipo,
            "auto_color": self.auto_color,
        }
