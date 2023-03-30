#--------------------------------------------#
#---                                      ---#
#---      Atividade 2 - Prestacao         ---#
#---           Profa: Ecila               ---#
#---  Quinta-feira, 23 de março de 2023   ---#
#---  Dev: Israel Alves Lucena Gomes      ---#
#---                                      ---#
#--------------------------------------------#


def main():
    """
    Função principal que organiza as entradas, o processamento e a saída

    O algorítmo 'Prestacao' irá calcular o valor da prestacao por meio da fórmula do juros simples
    utilizando como dados o valor inicial da prestacao[valInicial], a taxa de juros[taxa] (em %) e o tempo
    de atraso (em meses) do pagamento[tempo]. Com essas informações em mãos, calcularemos o
    valor final[valFinal] para o pagamento.

    valFinal = valInicial * [1 + (taxa * tempo * 1/100)]

    :return: int
    """

    # Etapa 1 - Declaração das variáveis utilizadas
    strEntrada: str = ''
    tempo: int = 0
    valInicial: float = 0.0
    valFinal: float = 0.0
    taxa: float = 0.0


    # Etapa 2 - Entrada e processamento da entrada do usuário
    print(f'\n\nOlá, usuário! Por favor, digite qual o valor inicial da sua dívida', sep='')
    strEntrada = input('---> ')

    if valorDecimalComErro(strEntrada):
        print("Olá, usuário... Você digitou um número inteiro, né?\n"
              "Bom... Infelizmente o número que digitou não é válido. Tente novamente.")
        exit(0)
    strEntrada = strEntrada.replace(',', '.')
    valInicial = float(strEntrada)

    print("Perfeito! Agora digite a taxa de juros (mensal) que o banco está cobrando")
    strEntrada = input('---> ')

    if valorDecimalComErro(strEntrada):
        print("Olá, usuário... Você digitou um número inteiro, né?\n"
              "Bom... Infelizmente o número que digitou não é válido. Tente novamente.")
        exit(0)
    strEntrada = strEntrada.replace(',', '.')
    taxa = float(strEntrada)

    print("Ótimo! Agora, por último, digite quantos meses essa conta está em atraso")
    strEntrada = input('---> ')

    if tempoComErro(strEntrada):
        print("Olá, usuário... Você digitou um número inteiro NÃO decimal, né?\n"
              "Bom... Infelizmente o número que digitou não é válido. Tente novamente.")
        exit(0)
    tempo = int(strEntrada)


    #Etapa 3 - Processamento
    valFinal = valInicial * (1 + taxa * tempo * 1/100)


    # Etapa 4 - Saída para o usuário
    print(f"\n\nO valor final da sua dívida é de R${valFinal}\n\n\n")

    return 1


def valorDecimalComErro(entradaDoUsuario: str) -> bool:
    """
    Essa função testará, por meio do try/except se o valor enviado pelo usuário é um número inteiro decimal ou
    ponto flutuante (float). Ela retornará False, caso o usuário tenha enviado um número decimal correto e
    retornará True caso tenha algum erro no número decimal enviado

    - O método replace da Classe string[entradaDoUsuario] substituirá todas as vírgulas por pontos, para assim,
    tentar converter a string em float.

    :param entradaDoUsuario:
    :return: bool
    """

    try:
        entradaDoUsuario = entradaDoUsuario.replace(',', '.')
        float(entradaDoUsuario)
        return False
    except:
        return True


def tempoComErro(entradaDoUsuario: str) -> bool:
    """
    Função que avalia se o usuário enviou uma informação correta. Ou seja se é um número inteiro.
    Esta função retornará False se a entrada for um caractere NÃO numérico e retornará True caso o usuário tenha
    digitado um número inteiro.

    - O método isnumeric da classe string[entradaDoUsuario] retorna verdadeiro quando todos os caracteres
    da string são numéricos. Caso contrário, retornará False.

    :return: bool
    """

    return not entradaDoUsuario.isnumeric()


main()