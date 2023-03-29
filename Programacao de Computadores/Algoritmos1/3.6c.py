# -----------------------------------------------------#
# Exercício 3.6 c)
# Calcula o valor final de uma divida/investimento a juros composto
# Dev: Israel Alves Lucena Gomes
# -----------------------------------------------------#

def main():
    valorInicial: float = 0
    taxaJuros: float = 0
    tempo: int = 0
    valorFinal: float = 0.0
    strEntrada: str = ''

    print("\n\nOlá usuário! Digite, por favor, o que se pede...")

    # Requisitando valor inicial
    strEntrada = input('---------> Valor inicial da dívida/investimento em R$:  ')
    if entradaErrada(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    strEntrada = strEntrada.replace(',', '.')
    valorInicial = float(strEntrada)

    # Requisitando taxa de juros
    strEntrada = input('---------> Taxa de juros mensal em %: ')
    if entradaErrada(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    strEntrada = strEntrada.replace(',', '.')
    taxaJuros = float(strEntrada)

    # Requisitando tempo
    strEntrada = input('---------> Tempo (meses) de duração/atraso: ')
    if entradaTempoComErro(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    tempo = int(strEntrada)

    print("Ei usuário! Confira, por favor, se os dados enviados estão corretos")
    print(f"\nValor inicial do investimento/dívida: R$ {valorInicial}")
    print(f"Taxa de juros mensal: {taxaJuros} %")
    print(f"Quantidade de meses de duração/atraso: {tempo}")

    print("\nConfirmar coordenadas e calcular a distância entre esses dois pontos")
    strEntrada = input("[S]im / [N]ão:  ")
    confirmaPontos = verificaConfirmacao(strEntrada)

    if not confirmaPontos:
        print("Hum... Olá de novo, usuário... Você não digitou a informação correta ou digitou Não/N.\nTente novamente!\n\n")
        exit(1)

    print("\nPerfeito! Fazendo continhas...")
    print(f"Valor final = R$ {calculaValorFinal(valorInicial, taxaJuros, tempo)}\n\n")

    return 1


def verificaConfirmacao(entradaUsuario: str) -> bool:
    """
    Verifica se o usuário digitou corretamente Sim/Não ao ser questionado e retorna True para situação
    na qual o usuário digitou S/Sim. Caso contrário ele retorna False

    :param entradaUsuario:
    :return:
    """

    if len(entradaUsuario) < 1:
        return False

    entradaUsuario = entradaUsuario.replace('[','').replace(']','')
    entradaUsuario = entradaUsuario.upper()

    if len(entradaUsuario) == 1 and entradaUsuario[0] == 'S':
        return True
    elif len(entradaUsuario) == 3 and entradaUsuario[0] == 'SIM':
        return True
    else:
        return False

def entradaErrada(entrada: str) -> bool:
    """
    Função que avalia se a entrada do usuário é decimal [ponto flutuante] (float)

    :param entrada:
    :return:
    """

    try:
        entrada = entrada.replace(',', '.')
        float(entrada)

        return False
    except:
        return True

def entradaTempoComErro(entradaDoUsuario: str) -> bool:
    """
    Função que avalia se o usuário enviou uma informação correta. Ou seja se é um número inteiro.
    Esta função retornará False se a entrada for um caractere NÃO numérico e retornará True caso o usuário tenha
    digitado um número inteiro.

    - O método isnumeric da classe string[entradaDoUsuario] retorna verdadeiro quando todos os caracteres
    da string são numéricos. Caso contrário, retornará False.

    :return: bool
    """

    return not entradaDoUsuario.isnumeric()

def calculaValorFinal(valorInicial: float, taxa: float, tempo: int) -> float:
    """
    Calula o valor final do juros por meio da fórmula.

    :param valorInicial:
    :param taxa:
    :param tempo:
    :return:
    """

    valorFinal: float = valorInicial * (1 + taxa / 100) ** tempo

    return valorFinal


main()