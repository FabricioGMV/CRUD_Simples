from flask import Flask, request
from controller.banco_controller import BancoController
from model.banco_users import BancoModel
from service.banco_service import BancoService

app = Flask(__name__)

@app.route("/")
def mostrar_usuarios():
    model = BancoModel()
    return model.dados_users_model()

@app.route("/cpf/<string:cpf>", methods=["GET"])
def criar_users(cpf):
    controller = BancoController()
    return controller.dicionario_controller(cpf)

@app.route("/cpf/<string:cpf>", methods=["DELETE"])
def apagar_usuario(cpf):
    controller = BancoController()
    return controller.deletar_users_controller(cpf)

@app.route("/criar", methods=["POST"])
def criar_usuario():
    criados = request.get_json()
    controller = BancoController()
    return controller.criar_users_controller(criados)