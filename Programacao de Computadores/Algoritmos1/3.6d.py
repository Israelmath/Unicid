# -----------------------------------------------------#
# Exercício 3.6 d)
# Decomposição de números
# Dev: Israel Alves Lucena Gomes
# -----------------------------------------------------#
from typing import List

def main():
    strEntrada: str = ''
    listaPosicional:List = []

    print("\n\nOlá usuário! Digite, por favor, o que se pede...")

    # Requisitando valor inicial
    strEntrada = input('---------> Digite um número natural entre 0 e 1000:  ')
    if entradaComErro(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    listaPosicional = contaAlgarismos(strEntrada)
    if len(listaPosicional) > 0:
        unidade: List = ['unidades', 'dezenas', 'centenas', 'unidades de milhar', 'dezenas de milhar', 'centenas de milhar']

        for index, valor in enumerate(listaPosicional):
            print(f"{listaPosicional[index]} {unidade[index]}")

    return 1


def entradaComErro(entradaDoUsuario: str) -> bool:
    """
    Função que avalia se o usuário enviou uma informação correta. Ou seja se é um número inteiro.
    Esta função retornará False se a entrada for um caractere NÃO numérico e retornará True caso o usuário tenha
    digitado um número inteiro.

    - O método isnumeric da classe string[entradaDoUsuario] retorna verdadeiro quando todos os caracteres
    da string são numéricos. Caso contrário, retornará False.

    :return: bool
    """

    if entradaDoUsuario.find('.') != -1 or entradaDoUsuario.find(',') != -1:
        return True

    return not entradaDoUsuario.isnumeric()


def contaAlgarismos(entradaDoUsuario: str) -> List:
    """
    Função que se utiliza de métodos matemáticos para fatorar a entrada do usuário em unidades de potências de 10.

    :param entradaDoUsuario:
    :return:
    """

    if not isinstance(entradaDoUsuario, str):
        return []

    else:
        entradaInt: int = int(entradaDoUsuario)
        listaPosicional = []

        if entradaInt == 0:
            return [0]

        while True:
            # Enquanto conseguir dividir por dez, adiciona à lista de unidades

            if entradaInt % 10 == 0 and entradaInt == 0:
                break
            else:
                listaPosicional.append(entradaInt % 10)
                entradaInt = entradaInt // 10

        return listaPosicional



main()