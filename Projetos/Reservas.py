#======================================================================================================================================================
#Sistema de Reservas e Cálculo de Pagamentos
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Programa conta com menu, validação de dados, estrutura de repetição,listas e arquivo txt
#Para o programa se tornar executavel devera ter um arquivo txt com o nome 'dados.txt' para armazenar as informações utilizadas no programa(obs:executado em 'onlinegdb.com')
#======================================================================================================================================================
#"os" utilizado para limpar saidas desnecessarias 
import os
#"re" utilizado para bloquear string numérica
import re
#datetime e pytz utilizados para fornecer a data e hora atual no fuso horário de Brasília
import datetime
import pytz
#PADRÃO PARA BLOQUEAR STRING NÚMERICA - (Métodos aplicados na condição 1 e 3)
padrao = r'^\d+$'
L1 = []
#l2 BARRA UMA POSSIVEL ENTRADA INVALIDA NO NOME DO RESPONSAVEL PELA RESERVA - (condição 1) e (condição 3)
l2 = ['','1','2','3','4','5','6','7','8','9','-','_','=','+','{','}','[',']','<','>',',','.',';','/',':','?','0','|','\\']
#L3 BARRA UMA POSSIVEL ALTERAÇÃO DE REGISTRO CASO A QUANTIDADE DE PESSOAS SEJA MAIOR QUE 6 - (condição 3)
l3 = [1, 2, 3, 4, 5, 6]
#L5 BARRA UMA POSSIVEL ENTRADA INVALIDA NO TIPO DE APARTAMENTO - (condição 3)
l5 = [1, 2]


while True:
    try:
        #MENU
        os.system('clear')
        print('''
\033[44;5;1m     Escolha uma opção:         
    [1] Reservar Apartamento    
    [2] Excluir Registro        
    [3] Alterar Registro        
    [4] Relatório               
    [5] SAIR                    \033[0m
        ''')
        opt = input("Escolha uma opção: ")

        if opt not in ["1", "2", "3", "4", "5"]:
            os.system('clear')
            print("OPÇÃO INVÁLIDA")
            input('PRESSIONE ENTER PARA VOLTAR AO MENU')
        #Condição 1    
        elif opt == '1':
            os.system('clear')
            print('\033[44;5;1mPreços por quantidade de pessoas e tipo de apartamento\033[0m\n')
            print('''\033[44;5;1mQuantidade de Pessoas    Diaria tipo 1    Diaria tipo 2 
            1                  20,00             25,00  
            2                  28,00             34,00  
            3                  35,00             42,00  
            4                  42,00             50,00  
            5                  48,00             57,00  
            6                  53,00             63,00  \033[0m\n''')

            resp = str(input('DIGITE O NOME DO RESPONSAVEL PELA RESERVA:\n'))
            os.system('clear')
            #condição que bloqueia string numérica
            if re.match(padrao, resp) or resp in l2:
                input('ERRO, PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
                continue
                os.system('clear')
            ps = int(input('Digite a quantidade de pessoas no apartamento:\n '))
            os.system('clear')

            if ps not in [1, 2, 3, 4, 5, 6]:
                print("Quantidade de pessoas inválida!")
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
                continue
            l3 = [1, 2, 3, 4, 5, 6]
            if ps not in l3:
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
            tp = int(input('Escolha uma opção\n\n\033[44;5;1m[1] DIARIA TIPO 1\n[2] DIARIA TIPO 2\033[0m\n'))
            if tp not in [1,2]:
                input('ERRO, PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
                continue
            os.system('clear')
            dias = int(input('DIGITE QUANTOS DIAS IRA PERMANECER NO APARTAMENTO\n'))
            os.system('clear')
          
#Estrutura condicional com operações que calculam o preço a pagar
            if ps == 1 and tp == 1:
                res = dias * 20.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            elif ps == 1 and tp == 2:
                res = dias * 25.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            elif ps == 2 and tp == 1:
                res = dias * 28.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            elif ps == 2 and tp == 2:
                res = dias * 34.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            elif ps == 3 and tp == 1:
                res = dias * 35.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            elif ps == 3 and tp == 2:
                res = dias * 42.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            elif ps == 4 and tp == 1:
                res = dias * 42.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            elif ps == 4 and tp == 2:
                res = dias * 50.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            elif ps == 5 and tp == 1:
                res = dias * 48.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            elif ps == 5 and tp == 2:
                res = dias * 57.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            elif ps == 6 and tp == 1:
                res = dias * 53.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            elif ps == 6 and tp == 2:
                res = dias * 63.00
                print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                os.system('clear')
            #Conversão de data e hora
            fuso_horario = pytz.timezone('America/Sao_Paulo')
            data_hora_atual = datetime.datetime.now(fuso_horario)
            data_hora_atual_str = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
            
            with open("dados.txt", 'a') as DB:
                linha = f"NOME: {resp}.    DIAS: {dias}.    TIPO: {tp}.    QUANTIDADE DE PESSOAS NO AP: {ps}.    PREÇO: {res}.    DATA E HORA: {data_hora_atual_str}\n"
                DB.write(linha)    
        #Condição 2        
        elif opt == '2':
            os.system('clear')
            with open("dados.txt", 'r') as DB:
                linhas = DB.readlines()

            if len(linhas) == 0:
                print("O arquivo está vazio.")
            else:
                print("Registros disponíveis para exclusão:")
                for index, linha in enumerate(linhas):
                    dados = linha.rstrip().split(',')
                    print(f"\033[44;5;1m[{index}] - {dados[0]}\033[0m")

                escolha = input("Digite o número do registro que deseja excluir ou pressione enter para voltar ao menu: ")
                os.system('clear')
                escolha = int(escolha)

                if escolha < 0 or escolha >= len(linhas):
                    print("Opção inválida.")
                else:
                    linhas.pop(escolha)  #Remove a linha 

                    with open("dados.txt", 'w') as DB:
                        for linha in linhas:
                            DB.write(linha)

                    print("\033[42;5;1mREGISTRO EXCLUÍDO COM SUCESSO.\033[0m")
                    input('\nPRESSIONE ENTER PARA VOLTAR AO MENU')
                    os.system('clear')
        #Condição 3            
        elif opt == '3':
            os.system('clear')
            with open("dados.txt", 'r') as DB:
                linhas = DB.readlines()
            if len(linhas) == 0:
                print("O arquivo está vazio.")
            else:
                print("Registros disponíveis para alteração:")
                for index, linha in enumerate(linhas):
                    dados = linha.rstrip().split(',')
                    print(f"\033[44;5;1m[{index}] - {dados[0]} \033[0m")

                escolha = input("Digite o número do registro que deseja alterar: ")
                os.system('clear')
                escolha = int(escolha)

                if escolha < 0 or escolha >= len(linhas):
                    print("Opção inválida.")
                else:
                    resp = str(input('Digite o novo nome do responsável pela reserva: '))
                    #condição que bloqueia string númerica
                    if re.match(padrao, resp) or resp in l2:
                        input('ERRO, PRESSIONE ENTER PARA VOLTAR AO MENU')
                        os.system('clear')
                        continue
                    os.system('clear')
                    ps = int(input('Digite a nova quantidade de pessoas no apartamento: '))
                    if ps not in [1, 2, 3, 4, 5, 6]:
                        print("Quantidade de pessoas inválida!")
                        input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                        os.system('clear')
                        continue
                    if ps not in l3:
                        input('ERRO, A QUANTIDADE DE PESSOAS SÃO NO MAXIMO 6, PRESSIONE ENTER PARA VOLTAR AO MENU')
                        os.system('clear')
                        continue
                    os.system('clear')
                    tp = int(input('Escolha uma nova opção\n\033[44;5;1m[1] DIARIA TIPO 1\n[2] DIARIA TIPO 2\033[0m\n'))
                    if tp not in l5:
                        input('ERRO, PRESSIONE ENTER PARA VOLTAR AO MENU')
                        continue
                    os.system('clear')
                    dias = int(input('Digite quantos novos dias irá permanecer no apartamento: '))
                    #Estrutura condicional com operações que calculam o preço a pagar
                    if ps == 1 and tp == 1:
                        res = dias * 20.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                        os.system('clear')
                    elif ps == 1 and tp == 2:
                        res = dias * 25.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                        os.system('clear')
                    elif ps == 2 and tp == 1:
                        res = dias * 28.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                        os.system('clear')
                    elif ps == 2 and tp == 2:
                        res = dias * 34.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                        os.system('clear')
                    elif ps == 3 and tp == 1:
                        res = dias * 35.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                        os.system('clear')
                    elif ps == 3 and tp == 2:
                        res = dias * 42.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                        os.system('clear')
                    elif ps == 4 and tp == 1:
                        res = dias * 42.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                        os.system('clear')
                    elif ps == 4 and tp == 2:
                        res = dias * 50.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                        os.system('clear')
                    elif ps == 5 and tp == 1:
                        res = dias * 48.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                        os.system('clear')
                    elif ps == 5 and tp == 2:
                        res = dias * 57.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                        os.system('clear')
                    elif ps == 6 and tp == 1:
                        res = dias * 53.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                        os.system('clear')
                    elif ps == 6 and tp == 2:
                        res = dias * 63.00
                        print(f'\033[42;5;1mO preço a pagar será {res}\033[0m')
                        input('PRESSIONE ENTER')
                    #Conversão de data e hora
                    fuso_horario = pytz.timezone('America/Sao_Paulo')
                    data_hora_atual = datetime.datetime.now(fuso_horario)
                    data_hora_atual_str = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
                    linhas[escolha] = f"NOME: {resp}.    DIAS: {dias}.    TIPO: {tp}.    QUANTIDADE DE PESSOAS NO AP: {ps}.    PREÇO: {res}.    DATA E HORA: {data_hora_atual_str}\n"
                    with open("dados.txt", 'w') as DB:
                        for linha in linhas:
                            DB.write(linha)
                    print("\033[42;5;1mRegistro alterado com sucesso.\033[0m")
                    input('PRESSIONE ENTER PARA VOLTAR AO MENU')
                    os.system('clear')
        #Condição 4            
        elif opt == '4':
            os.system('clear')
            with open("dados.txt", 'r') as DB:
                linhas = DB.readlines()

            if len(linhas) == 0:
                print("O arquivo está vazio.")
            else:
                print("Relatório de registros:\n")
                for linha in linhas:
                    print(f"\033[44;5;1m{linha.rstrip()}\033[0m")

            input('\nPRESSIONE ENTER PARA VOLTAR AO MENU')
            os.system('clear')
        #Condição 5    
        elif opt == '5':
            os.system('clear')
            print('\033[42;5;1mPROGRAMA FINALIZADO\033[0m')
            break
    except ValueError:
        NameError
        os.system('clear')
        print('ERRO, O MENU FOI REINICIADO')