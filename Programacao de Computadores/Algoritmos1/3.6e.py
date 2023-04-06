# -----------------------------------------------------#
# Exercício 3.6 e)
# Caixa eletetrônico básico
# Dev: Israel Alves Lucena Gomes
# -----------------------------------------------------#
from typing import List

def main():
    strEntrada: str = ''
    valorASacar: int = 0
    dictNotasQtds: dict = {
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0
    }

    print("\n\nOlá usuário! Digite, por favor, o que se pede...")

    # Requisitando valor inicial
    strEntrada = input('---------> Qual o valor que deseja sacar?   ')
    if entradaComErro(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    valorASacar = int(strEntrada)

    dictNotasQtds = contaNotas(dictNotasQtds, valorASacar)
    print("\nCédulas a devolver:")
    for chave, valor in dictNotasQtds.items():
        print(f"{valor} cédulas de {chave} = R$ {chave*valor}")

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


def contaNotas(notas: dict, valorCalcular: int) -> dict:
    """
    Essa função itera sobre o dicionário de cédulas possíveis. Dentro de um loop, calcula a quantidade de cédulas que
    são necessárias para ultrapassar o valor e adiciona a quantidade antes de ultrapassar.

    :param notas:
    :param valorCalcular:
    :return: dicionário contendo as notas em reais (keys) e a quantidade de cada nota (values)
    """

    for valor in notas.keys():
        proximaNota: bool = False

        while not proximaNota:
            if valor * notas[valor] > valorCalcular:
                notas[valor] = notas[valor] - 1
                valorCalcular -= valor * notas[valor]
                proximaNota = True
            else:
                notas[valor] += 1

    return notas






main()