from entidades.usuario import Usuario
from utils import Utils
from config.data_manager import session
from entidades.usuario import Usuario

class UsuarioManager:

    @classmethod
    def cadastrar_usuario(cls):

        while True:
            nome = input("Nome: ")
            cpf = input("Cpf: ")
            email = input("E-mail: ")
            senha = input("Senha: ")

            usuario = Usuario(cpf, nome, email, senha)
            session.add(usuario)
            session.commit()

            print(f"\nUsuário {usuario.nome} cadastrado com sucesso!")

            if not Utils.deseja_continuar():
                break


    @classmethod
    def editar_usuario(cls):

        while True:

            lista_usuarios = session.query(Usuario).all()

            for usuario in lista_usuarios:
                usuario.listar_usuario_e_cpf()

            cpf = input("\nDigite o CPF do usuário que será alterado: ")

            usuario = session.query(Usuario).filter_by(cpf=cpf).first()
            print(usuario)

            atr = Utils.formatar_texto(input("\nDigite o atributo que será alterado: "))

            if atr == "usuario":

                new_atr = input(f"Você deseja trocar o seu [ NOME > {usuario.nome} ] por: ")
                usuario.nome = new_atr
                session.commit()

                print("\nAtributo alterado com sucesso!")

            elif atr == "cpf":

                new_atr = input(f"Você deseja trocar o seu [ CPF > {usuario.cpf} ] por: ")
                usuario.cpf = new_atr
                session.commit()

                print("\nAtributo alterado com sucesso!")

            elif atr == "email":

                new_atr = input(f"Você deseja trocar o seu [ E-MAIL > {usuario.email} ] por: ")
                usuario.email = new_atr
                session.commit()

                print("\nAtributo alterado com sucesso!")

            elif atr == "senha":

                new_atr = input(f"Você deseja trocar o seu [ E-MAIL > {usuario.senha} ] por: ")
                usuario.senha = new_atr
                session.commit()

                print("\nAtributo alterado com sucesso!")

            if not Utils.deseja_continuar():
                break


    @classmethod
    def listar_usuario(cls):

        while True:
            print("Lista de Usuários:")
            lista_usuarios = session.query(Usuario).all()

            for usuario in lista_usuarios:
                print(usuario)

            if not Utils.deseja_continuar():
                break

    @classmethod
    def excluir_usuario(cls):

        while True:
            lista_usuarios = session.query(Usuario).all()

            for usuario in lista_usuarios:
                usuario.listar_usuario_e_cpf()

            cpf = input("\nDigite o CPF do usuário que será excluido: ")

            usuario = session.query(Usuario).filter_by(cpf=cpf).first()
            session.delete(usuario)
            session.commit()

            print("\nUsuário excluido com sucesso!")

            if not Utils.deseja_continuar():
                break