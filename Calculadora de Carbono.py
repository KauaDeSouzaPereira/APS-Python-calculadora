import math

# função calculo de carbono de cigarro e energia
def calculo(qtscigarro,egeletrica):

    valeletric = egeletrica * 0.1

    valciga = qtscigarro * 0.02

    return valciga + valeletric

# Calcula como compensar a emissão caso haja prejuízo
def calcular_compensacao(retrasado,opcao):
    if opcao == 1:
        valor = (retrasado / 1000) * -1

        return valor, f"Para compensar sua emissão, compre R${round(valor):.2f} ou U${valor * 5.35:.2f}"

    elif opcao == 2:
        arvores = (retrasado / 1000) * -8

        return arvores, f"Você precisa plantar {math.ceil(arvores)} árvore(s)"

    else:
        return 0, "Opção inválida."

# função calculo de carbono de ônibus
def distribuicao(qtdcaminhoes):
    valcombustivel = int(qtdcaminhoes) * 50
    
    if qtdcaminhoes > 0:
        return valcombustivel


# Começo do programa
print("=== Cálculo de Pegada de Carbono da Empresa ===")



emptrab = input('Sua empresa trabalha com cigarros ? ')
if emptrab.lower() == 'não':
    print("\n=== Programa finalizado ===")
    end()

# Dados da empresa
qtdcigar = int(input('Quantos cigarros sua empresa vende por mês? '))
energiaEletric = float(input('Quanto que a sua empresa gasta de KWH por mês? '))

# Distribuição caso a empresa faça
qtdtruck = input('Sua empresa realiza a distribuição por conta própria? Se sim quantas por mês? ')

# Calculo de carbono
while True:

    if qtdtruck.lower() == 'não':
        totalcarb = calculo(qtscigarro = qtdcigar, egeletrica = energiaEletric) * 12

    else:
        qtdtruck = int(qtdtruck)
        totalcarb = calculo(qtscigarro = qtdcigar, egeletrica = energiaEletric) + distribuicao(qtdcaminhoes = qtdtruck) * 12
    
    break

print(f'\nSua empresa gasta: {totalcarb} de kilos de carbono\n')

# Pega o valor do ano passado
retrasado = float(input('Qual foi a emissão de carbono da sua empresa no ano retrasado? '))

# calculo de comparação de lucro e perda
retrasado =  totalcarb - retrasado

# Condição caso a empresa lucre
if retrasado > 0:
    print(f'\nVocê teve um lucro de R${retrasado:.2f}')

    
    vender = input('\nVocê deseja vender o seu crédito de carbono para outras empresas? ').lower()

    # Dando opcões para vender crédito de carbono
    while True:
        try:
            if vender == 'sim':
                opcao = int(input('Essas são as empresas que nós sugerimos para você: 1-O boticario e 2-Amazon\n'))

                if opcao == 1:
                    print('Link Oboticário: https://www.boticario.com.br/?&utm_source=google&utm_medium=cpc&utm_campaign=18281460401_137894085741&ds_rl=1270144&gclid=CjwKCAiA68ebBhB-EiwALVC-NmsFbK_7z6WJ4Z7FGmNg8vJ2Svzsu0F-3CPxWgno1jhIURwUuccBNBoC_1AQAvD_BwE&gclsrc=aw.ds')

                    break

                elif opcao == 2:
                    print('Link Amazon: https://www.amazon.com.br/?tag=hydrbrgk-20&hvadid=558683589546&hvpos=&hvexid=&hvnetw=g&hvrand=9695004996668470602&hvpone=&hvptwo=&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001655&hvtargid=kwd-15305691825&ref=pd_sl_7ddjoi3zeb_e')  

                    break

                else:
                    print('Opção Inválida! Digite 1 ou 2')

            # Caso não queira vender
            else:
                print(f'Ok, seu lucro ficou em R${retrasado:.2f}')

                break

        except ValueError:
            print('Você digitou um número inválido! Digite apenas 1 ou 2.')

# Condição caso a empresa tenha perda
elif retrasado < 0:
    print(f'\nVocê teve uma perda de R${abs(retrasado):.2f}\n')

    # Dando opções para comprar créditos de carbono
    while True:
        try:
            compra = int(input('Você deseja comprar créditos de carbono (1) ou (2) plantar arvores? '))

            if compra in [1, 2]:
                valor, mensagem = valor, mensagem = calcular_compensacao(retrasado,compra)

                print(mensagem)

                break

            else: 
                print('Opção Inválida! Digite 1 ou 2')

        except ValueError:
            print('Opcão Inválida! Digite 1 ou 2')

# Condição caso não tenha nenhuma alteração
else :
    print('\nVocê não teve lucro, nem perda nesse ano.')

        
# fim do programa
print("\n=== Programa finalizado ===")