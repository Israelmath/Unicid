#--------------------------------------------#
#---                                      ---#
#---      Atividade 1 - Salario           ---#
#---           Profa: Ecila               ---#
#---  Quinta-feira, 23 de março de 2023   ---#
#---  Dev: Israel Alves Lucena Gomes      ---#
#---                                      ---#
#--------------------------------------------#


def main():
    """
    Função principal que organiza as entradas, o processamento e a saída

    O algorítmo 'Salario' recebe uma entrada com a quantidade de softwares que o desenvolvedor escreveu e
    devolve seu salário a partir da fórmula abaixo. A saber, a variável 'qtdSoftwares' indica a quantidade de
    programas desenvolvidos.

    salario = 50 * qtdSoftwares + 500

    :return: int
    """

    # Etapa 1 - Declaração das variáveis utilizadas
    strEntrada: str = ''
    qtdSoftwares: int = 0
    salarioDev: float = 0.0


    # Etapa 2 - Entrada do usuário
    print(f'\n\nOlá, usuário! Por favor, digite quantos softwares o desenvolvedor escreveu', sep='')
    strEntrada = input('---> ')


    #Etapa 3 - Processamento
    # Etapa 3.1 - Processa entrada
    if entradaComErro(strEntrada):
        print("Olá, usuário... Você digitou um número inteiro, né?\n"
              "Bom... Infelizmente o número que digitou não é válido. Tente novamente.")
        exit(0)

    # Etapa 3.2 - Processamento das informações enviadas
    qtdSoftwares = int(strEntrada)
    salarioDev = 50 * qtdSoftwares + 500


    # Etapa 4 - Saída para o usuário
    print(f"\n\nO salário do desenvolvedor é de R${salarioDev}\n\n\n")

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

    return not entradaDoUsuario.isnumeric()


main()