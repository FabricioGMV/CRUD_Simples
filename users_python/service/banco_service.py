from model.banco_users import BancoModel

class BancoService:
    def banco_usuario_service(self, cpf):
        bd = BancoModel()
        banco = bd.dados_users_model()

        for c in banco:
            if(c ['cpf'] == cpf):
                return c
            
        return {"erro": "CPF não encontrado"}, 404
            
    def delete_users_service(self, cpf):
        bd = BancoModel()
        banco = bd.dados_users_model()

        for usuario in banco:
            if(usuario ['cpf'] == cpf):
                banco.remove(usuario)
                return {"Mensagem": "CPF removido da lista com sucesso."}
            
        return {"erro": "CPF não encontrado"}, 404
    
    def criar_users_service(self, dados):
        bd = BancoModel()
        banco = bd.dados_users_model()
        camp_obg = ["nome", "email", "senha", "cpf"]

        for campo in camp_obg:
            if(campo not in dados):
                return {"erro": f"Campo(s) obrigatório(s) faltantes(s): {campo}"}, 400
        

        banco.append(dados)

        return {"mensagem": "Usuário(s) criados com sucesso."}