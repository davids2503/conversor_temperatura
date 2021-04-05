resposta='S'
while resposta =='S':
    menu_Temperatura = "O que você quer converter?" "\n 1- Celcius em Fahrenheit" "\n 2- Fahrenheit em Celcius"
    print(menu_Temperatura)
    opc = int(input("Digite sua resposta: "))
    if opc == 1:
        cel = int(input("Digite quantos graus você quer converter: "))
        cel1 = cel * float(1.8) + 32
        print(cel, "grau(s)", "Celcius", "são", cel1, "graus", "em Fahrenheit")
    elif opc == 2:
        fah = float(input("Digite quantos graus você quer converter: "))
        fah1 = fah - 32
        fah2 = int(fah1 * 5 / 9)
        print(fah," grau(s)", "Fahrenheit", "são", fah2,"graus", " em Celcius")
    else:
        print("Digite a opção correta")
    resposta=input("Digite \"S\" para realizar nova conversão: ").upper()
