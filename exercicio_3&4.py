#!/usr/bin/python
import sys
################################# - Resolução dos exercícios 3 e 4 - ########################################
################################ - Função para adicionar retangulo - ##########################################
def add_ret():

    A = [int(input("Entre com x1:")), int(input("Entre com y1:")), int(input("Entre com x2:")), int(input("Entre com y2:"))]

    return A
################################ - O método utilizado na resolução possui algumas particularidades - ##########################################
# o primeiro par de A é o par ordenado mais próximo da origem e o segundo o mais distante, se for passado como parametro da forma contrária
# a função extremidades adequa para que a solução possa ser utilizada.
def extremidades(A):
    if(A[0]>A[2]):
        aux = A[0]
        A[0] = A[2]
        A[2] = aux
    if(A[1]>A[3]):
        aux = A[1]
        A[1] = A[3]
        A[3] = aux
    return A
################################ - Função para verificar se há interseção entre os retangulos- ##########################################
def intersects(A, B):
    cond_x1 = (B[0] > A[0]) and (A[2] > B[0])
    cond_y1 = (B[1] < A[1]) and (A[1] < B[3])
    cond_x2 = cond_x1
    cond_y2 = (A[1] < B[1]) and (B[1] < A[3])
    if ((cond_x1) and (cond_y1)) or (cond_y2):
        return (True, cond_y1, cond_y2)
    else:
        return (False, 0)
################################ - Função para calcular o valor da área de interseção- ##########################################
def calcula_area(resp):
    if ((resp[0]) and (resp[1])):
        return ((A[2]-B[0])*(B[3]-A[1]))
    elif ((resp[0]) and (resp[2])):
        return ((A[2]-B[0])*(A[3]-B[1]))
    else:
        return 0

def main():
    continuar = 1
    while (continuar):
        print("Coordenadas do primeiro retângulo:")
        A = add_ret()
        print("Coordenadas do segundo retângulo:")
        B = add_ret()

        resp = intersects(A, B)
        print(f'intersects(A, B) => {resp[0]}')
        continuar = int(input("Digite 0 para parar e 1 para testar outros dois retangulos: "))

    aux = input("Para calcular a area de interseção digite s, caso contrário pressione qualquer tecla: ")

    if (aux == 's'):
        print("###### Resposta do exercício 4 ######")
        print(f'A área de interseção é: {calcula_area(resp)} u.a (unidades de área)')
    else:
        sys.exit()

main()