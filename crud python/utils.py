import unicodedata
import re

class Utils:

    @staticmethod
    def deseja_continuar():
        while True:
            opt = input("Deseja continuar? [S] - [N]").strip().upper()

            if opt == "S":
                return True

            elif opt == "N":
                return False

            else:
                print("Opção inválida, tente novamente...")

    @staticmethod
    def formatar_texto(texto):

        #Tira acento do texto
        texto = unicodedata.normalize('NFKD', texto)
        texto = ''.join(c for c in texto if not unicodedata.combining(c))

        #Tira símbolos do texto
        texto = re.sub(r'[^a-zA-Z0-9 ]', '', texto)

        return texto.lower()

