#-----------------------------------------------------#
# Exercício 3.6 a)
# Área do triângulo, usando a fórmula do semicírculo
# Dev: Israel Alves Lucena Gomes
#-----------------------------------------------------#

def main():
    ladoA: float = 0
    ladoB: float = 0
    ladoC: float = 0
    areaDoTriangulo: float = 0
    strEntrada: str = ''

    # Requisitando lado A do triângulo
    print("\n\nDigite o lado A do triângulo:", sep='')
    strEntrada = input('---------> Lado A: ')

    if entradaErrada(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    strEntrada = strEntrada.replace(',', '.')        
    ladoA = float(strEntrada)
    
    # Requisitando lado B do triângulo
    print("Digite o lado B do triângulo:", sep='')
    strEntrada = input('---------> Lado B: ')

    if entradaErrada(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    strEntrada = strEntrada.replace(',', '.')        
    ladoB = float(strEntrada)

    # Requisitando lado C do triângulo
    print("Digite o lado C do triângulo:", sep='')
    strEntrada = input('---------> Lado C: ')

    if entradaErrada(strEntrada):
        print(f"Acho que você não digitou um número válido. Reinicie o programa e tente novamente...")
        exit(0)
    strEntrada = strEntrada.replace(',', '.')        
    ladoC = float(strEntrada)

    if not ehTriangulo(ladoA, ladoB, ladoC):
        print("""Infelizmente, os três valores que digitou não formam um triângulo, pois a soma de dois lados do triângulos é menor do que o terceiro lado.""")
        exit(0)


    # Iniciando processamento
    print("    \n\nCalculando a área do triângulo informado...")
    areaDoTriangulo = calculaArea(ladoA, ladoB, ladoC)

    print(f"A área do triângulo é: {areaDoTriangulo}")

    return 1

def entradaErrada(entrada: str) -> bool:
    # Função que avalia se a entrada do usuário é 
    # decimal [ponto flutuante] (float)

    try:
        entrada = entrada.replace(',', '.')
        float(entrada)

        return False
    except:
        return True

def ehTriangulo(ladoA: float, ladoB: float, ladoC: float) -> bool:
    """
    A regra da matemática para que uma figura geométrica seja um triângulo,
    é de que a soma de dois lados sempre seja menor do que o outro lado.

    Essa função retorna True, caso essa propriedade seja satisfeita.
    """

    ladosAB = ladoA + ladoB
    ladosAC = ladoA + ladoC
    ladosBC = ladoB + ladoC

    if ladosAB <= ladoC:
        print("""LadoA + LadoB <= LadoC""")
        return False
    elif ladosAC <= ladoB:
        print("""LadoA + LadoC <= LadoB""")
        return False
    elif ladosBC <= ladoA:
        print("""LadoB + LadoC <= LadoA""")
        return False
    else:
        return True

def calculaArea(ladoA: float, ladoB: float, ladoC: float) -> float:
    semicirculo: float = 0
    
    semicirculo = calculaSemicirculo(ladoA, ladoB, ladoC)
    area = (semicirculo * (semicirculo - ladoA) * (semicirculo - ladoB) * (semicirculo - ladoC))**0.5

    return area

def calculaSemicirculo(ladoA: float, ladoB: float, ladoC: float) -> float:
    return (ladoA + ladoB + ladoC) / 2



main()