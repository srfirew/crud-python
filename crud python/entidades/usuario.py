from sqlalchemy import Column, String, Integer
from config.data_manager import Base
from sqlalchemy import func
from config.data_manager import session

class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True)
    cpf = Column("cpf", String(100))
    nome = Column("nome", String(100))
    email = Column("email", String(100))
    senha = Column("senha", String(100))


    def __init__(self, cpf, nome, email, senha):

        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"\nUsuário: {self.nome} \nCPF: {self.cpf} \nE-mail: {self.email} \nSenha: {self.senha}"


    def listar_usuario_e_cpf(self):
        print(f"\nUsuário: {self.nome} \nCPF: {self.cpf}")







