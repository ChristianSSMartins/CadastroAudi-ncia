import sys
import os
from datetime import datetime

cadastro = 1

while cadastro == 1:
    print("Seja bem vindo ao cadastro de audiências \n")
    # Requerimento das informações {
    a = 1
    while a == 1:
        new = input("Você deseja cadastrar uma nova audiência? (sim/não)")
        if new == "sim" or new == "Sim":
            os.system('cls') or None
            print("Por favor, digite as informações necessárias para o cadastro! \n")

            b = False
            while b == False:
                try:
                    date = input("Digite a data da audiência separando dia, mês e ano (xx/xx/xxxx) : ")
                    print("")
                    dt = datetime.strptime(date, '%d/%m/%Y').date()
                    b = True
                except:
                    print("Data no formato incorreto, digite novamente!")

            c = False
            while c == False:
                try:
                    time = input("Digite a hora da audiênia separando hora e minuto com (:): ")
                    print("")
                    tm = datetime.strptime(time, '%H:%M').time()
                    c = True
                except:
                    print("Hora no formato incorreto, digite novamente!")

            lowyer = input("Digite o nome do advogado que ira participar da audiência: ")
            print("")
            forum = input("Digite o nome do fórum onde ocorrera a audiência: ")
            print("")
            endress = input("Digite o endereço do fórum separando o número com vírgula (R.xxxx, 000): ")
            print("")

            f = 1
            while f == 1:
                num = input("Digite o número do processo: ")
                if len(num) == 6:
                    f = 2
                else:
                    print("O número do processo deve conter 6 caracteres, digite o número novamente! \n")
            a = 2

        elif new == "não" or new == "Não":
            os.system('cls') or None
            print("Obrigado por acessar nosso sistema!")
            a = 2
            exit()
        else:
            print("Digite uma opção válida! (sim/não)")
    # }
    # Confirmar e salvar os dados {
    d = 1
    while d == 1:
        conf = input(
            "Seus dados foram registrados, deseja conferir os dados? (sim/não)")
        if conf == "sim" or conf == "Sim":
            os.system('cls') or None
            print("Data escolhida para a audiência: " +str(dt.strftime("%d/%m/%Y")))
            print("")
            print("Hora escolhida para a audiência: " + str(tm))
            print("")
            print("Advogado escolhido para a audiência: " + str(lowyer))
            print("")
            print("Fórum escolhido para a audiência: " + str(forum))
            print("")
            print("Endereço do fórum escolhido para a audiência: " + str(endress))
            print("")
            print("Número do processo da audiência: " + str(num))
            print("")
            d = 2
        elif conf == "não" or conf == "Não":
            # Salvar os dados no DB
            os.system('cls') or None
            print("Seu casastro foi salvo!")
            print("Obrigado por acessar nosso sistema!")
            d = 2
            exit()
        else:
            print("Digite um opção válida!) (sim/não")
    # }
    # Exclusão dos dados {
    e = 1
    while e == 1:
        regis = input("Desejá editar esse cadastro? (sim/não)")
        if regis == "sim" or regis == "Sim":
            os.system('cls') or None
            print("Cadastro apagado com sucesso")
            e = 2
        elif regis == "não" or regis == "Não":
            os.system('cls') or None
            print("Seu casastro foi salvo!")
            print("Obrigado por acessar nosso sistema!")
            e = 2
            cadastro = 2
        else:
            print("Digite uma opção válida! (sim/não)")
    # }
