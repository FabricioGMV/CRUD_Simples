from service.banco_service import BancoService

class BancoController:
    def dicionario_controller(self, cpf):
        service = BancoService()
        return service.banco_usuario_service(cpf)
    
    def deletar_users_controller(self, cpf):
        service = BancoService()
        return service.delete_users_service(cpf)
    
    def criar_users_controller(self, criados):
        service = BancoService()
        return service.criar_users_service(criados)