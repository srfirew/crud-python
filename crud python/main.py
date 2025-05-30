from services.usuario_manager import UsuarioManager
from config.data_manager import db, Base
from entidades.usuario import Usuario

Base.metadata.create_all(bind=db)

def menu():
    print("\nEscolha uma opção: \n")
    print("[1] - Cadastrar usuário ")
    print("[2] - Editar usuário ")
    print("[3] - Remover Usuário ")
    print("[4] - Listar usuários ")
    print("[5] - Sair ")

while True:

    menu()

    opt = input("")

    if opt == "1":

        UsuarioManager.cadastrar_usuario()

    elif opt == "2":

        UsuarioManager.editar_usuario()

    elif opt == "3":

        UsuarioManager.excluir_usuario()

    elif opt == "4":

        UsuarioManager.listar_usuario()

    elif opt == "5":
        break

    else:
        print("Opção inválida, tente novamente...")



