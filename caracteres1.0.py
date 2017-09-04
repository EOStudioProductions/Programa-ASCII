valor = 0
caracter = ""
menu = ""
exit = ""

print()
print(150 * "=")
print(150 * "-")
print(150 * "=")
print()
print("""Quer descobrir quais os caracteres que existe dentro do seu computado? Então utilize o programa conforme as instruções abaixo:


*O programa sempre inicia do valor 0*
----------------------------------------------------------------------------------------
*Digite o valor desejado que o programa irá percorrer do 0 até o valor que você digitou*

""")
print("Programa Iniciado...")
print("""

       ##################################################
      #
     #  
    #   
   #         *  ********  *********  ***********        *   ********
  #          *  *         *          *         *        *   *
 #      ******  *****     *          *         *   ******   *****
#      *     *  *         *          *         *  *     *   *
#       ******  ********  *********  ***********   ******   ********
# O programa da decodificação ASCC.
####################################################################
""")
print("Você deseja descobrir uma sequência de caractéres, ou algum caracter específico?")
while exit != "sair":
    menu = input("Digite caracter para a opção caracter específico, ou digite sequência para a opção sequência de caractéres: ")
    while ((menu != "sequência") and (menu != "caracter")):
        print(">>ERROR!<<", "Digite um valor válido!")
        menu = input("Digite caracter para a opção caracter específico, ou digite sequência para a opção sequência de caractéres: ")    
    if menu == "sequência":
        valor = int(input("Digte um valor, cujo, será percorrido e mostrado a sequência de caractéres: "))
        for c in range(valor):
            print(str(c), " - ", chr(c))
    else:
        caracter = input("Digite o caracter conrrespondente para saber o seu devido valor: ")
        print(caracter, " - ", ord(caracter))
    exit = input("Digite sair se desejar sair do programa: ")
    print()
    print(50*"=")
    print()