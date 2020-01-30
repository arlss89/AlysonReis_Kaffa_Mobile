#Função para verificar se a entrada pode ser um cnpj
'''Esta primeira função irá retornar alguns parâmetros do cnpj para verificação e posterior validação do mesmo.
Assim, pode-se verificar a solução dos exercícios 1 e 2 do teste
'''
def verif_cnpj(cnpj):
    #Para retirar os caracteres nao numéricos do cnpj
    cnpj = cnpj.replace("-", "")
    cnpj = cnpj.replace(".", "")
    cnpj = cnpj.replace("/", "")
    #cnpj = cnpj.replace(" ", "")
    ult_2_dig = cnpj[-2:]

    return (cnpj, len(cnpj), ult_2_dig)   #Retornando parâmetros que serão utilizados durante o programa

def verif_cnpj_valido(cnpj):              #Função para verificar se o cnpj é, de fato, válido (parte do exercício 2)
    '''OBS. Fórumula atualizada em 29/01/2020, às 23h

    Para calcular os dígitos validadores do cnpj os seguintes passos serão seguidos:

    ***Para calcular o 1º dígito verificador:
        a) Cada um dos doze primeiros números do CNPJ, a partir do 12º número até o 1º,
        é multiplicado por um peso que começa de 2 e que vai sendo incrementado de 1 a cada passo,
        somando-se as parcelas calculadas. Sempre que o peso atingir o valor 10 ele deve novamente receber o valor inicial 2

        b) calcula-se o dígito através da seguinte expressão: soma % 11 = resto
        OBS. se o resto da divisão (operador %) calculado for 0 ou 1, o dígito verificador será 0;
        nos outros casos, o dígito verificador é definido pela expressão: 11 - resto = dig1

    ***Para calcular o 2º dígito verificador:
        a) Cada um dos treze primeiros números do CNPJ, a partir do primeiro DV (13º número) até o 1º,
        é multiplicado por um peso que começa de 2 e que vai sendo incrementado de 1 a cada passo,
        somando-se as parcelas calculadas. Sempre que o peso atingir o valor 10 ele deve novamente receber o valor inicial 2

        b) calcula-se o dígito através da seguinte expressão: soma % 11 = resto
        OBS. se o resto da divisão (operador %) calculado for 0 ou 1, o dígito verificador será 0;
        nos outros casos, o dígito verificador é definido pela expressão: 11 - resto = dig2

        '''

    cnpj = list(map(int, cnpj))                     #Tranforma a string cnpj em uma lista de caracteres, que posteriormente serão convertidos em número

    #Calculo do primeiro digito verificador
    peso = 2
    soma = 0
    i = 11                                          #O indice do vetor começa em 0 e a 12ª posição corresponde ao indice 11
    while(i!=0):                                    #regra a) do primeiro digito
        soma = peso*cnpj[i]+soma
        peso = peso+1
        if(peso==10):
            peso = 2
        i = i-1

    resto = soma%11
    if(resto==0 or resto==1):                       #Regra b) do primeiro digito
        dig1 = 0
    else:
        dig1 = 11-resto

    #Calculo do segundo dígito verificador
    peso = 2
    soma = 0
    i = 12
    while (i != 0):  # regra a) do segundo digito
        soma = peso * cnpj[i] + soma
        peso = peso + 1
        if (peso == 10):
            peso = 2
        i = i - 1

    resto = soma % 11
    if (resto == 0 or resto == 1):  # Regra b) do segundo digito
        dig2 = 0
    else:
        dig2 = 11 - resto
    return (str(dig1)+str(dig2))

#main

cnpj = input("Entre com o cnpj: \n")
verif = verif_cnpj(cnpj)

if((verif[1]==14)and(type(int(verif[0])))): #caso o usuário entre com uma letra, entre os 14 elementos do cnpj, type(int(verif[0])) será Falso
    print("Ok, os caracteres podem ser um cnpj válido.")
    print("########### Validação requerida no exercício 2 ###########")
    validar = int(input("Digite 0 para sair ou 1 para validar: "))
    if(validar):
        cnpj = verif[0]
        if(verif_cnpj_valido(cnpj) == verif[2]):
            print("\nEste CNPJ é válido!")
    else:
        exit()
else:
    print("cnpj inválido")

