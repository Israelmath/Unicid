#-----------------------------------------------------#
# Exercício 3.6 b)
# Calcula a distância entre dois pontos
# Dev: Israel Alves Lucena Gomes
#
# Dadas as coordenadas de 2 pontos num plano (X1, Y1) , (X2, Y2), calcular a 
# distância entre esses pontos
#-----------------------------------------------------#

def main():
    pontoXA: float = 0
    pontoYA: float = 0
    pontoXB: float = 0
    pontoYB: float = 0
    confirmaPontos: bool = False
    distancia: float = 0.0
    strEntrada: str = ''

    # Requisitando lado A do triângulo
    print("\n\nOlá, usuário! Digite, por favor, digite o que se pede:", sep='')

    strEntrada = input('---------> Coordenada X do ponto A: ')
    if entradaErrada(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    strEntrada = strEntrada.replace(',', '.')
    pontoXA = float(strEntrada)

    strEntrada = input('---------> Coordenada Y do ponto A: ')
    if entradaErrada(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    strEntrada = strEntrada.replace(',', '.')
    pontoYA = float(strEntrada)

    strEntrada = input('---------> Coordenada X do ponto B: ')
    if entradaErrada(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    strEntrada = strEntrada.replace(',', '.')
    pontoXB = float(strEntrada)

    strEntrada = input('---------> Coordenada Y do ponto B: ')
    if entradaErrada(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    strEntrada = strEntrada.replace(',', '.')
    pontoYB = float(strEntrada)

    print("\n\nPerfeito! Confira as coordenadas que você digitou...")
    print(f"A: ({pontoXA}, {pontoYA})")
    print(f"B: ({pontoXB}, {pontoYB})")

    print("Confirmar coordenadas e calcular a distância entre esses dois pontos")
    strEntrada = input("[S]im / [N]ão:  ")
    confirmaPontos = verificaConfirmacao(strEntrada)

    if not confirmaPontos:
        print("Hum... Olá de novo, usuário... Você não digitou a informação correta ou digitou Não/N.\nTente novamente!\n\n")
        exit(1)

    print("\n\n----> Perfeito, usuário! Vou calcular a distância desses dois pontos enviados")
    distancia = calculaDistancia(pontoXA, pontoYA, pontoXB, pontoYB)

    print(f"\n\nA: ({pontoXA}, {pontoYA})")
    print(f"B: ({pontoXB}, {pontoYB})")
    print(f"d(A, B) = {distancia}\n\n")

    return 0

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

def calculaDistancia(pontoXA: float, pontoYA: float, pontoXB: float, pontoYB: float) -> float:
    """
    Calcula as diferenças entre as coordenadas X e Y e a raiz quadrada da soma entre esses dois valores.

    :param pontoXA: Coordenada X do ponto A
    :param pontoYA: Coordenada Y do ponto A
    :param pontoXB: Coordenada X do ponto B
    :param pontoYB: Coordenada Y do ponto B
    :return: Retorna a distância entre os dois pontos dados
    """

    difX: float = quadradoDaDiferenca(pontoXA, pontoXB)
    difY: float = quadradoDaDiferenca(pontoYA, pontoYB)

    return (difX + difY) ** 0.5

def quadradoDaDiferenca(coordenadaA: float, coordenadaB: float) -> float:
    """
    Calcula o quadrado da diferença/subtração entre dois números

    :param coordenadaA:
    :param coordenadaB:
    """

    return (coordenadaB - coordenadaA) ** 2


main()