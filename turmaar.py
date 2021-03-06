turma = []
cpfs = []

#PARA SALVAR A TURMA
def salvar_turma():
    global turma
    arquivo = open("turmas.txt", "w", encoding="utf-8")
    for i in turma:
        cod_turma = str(i[0])
        periodo = str(i[1])
        cod_disciplina = str(i[2])
        cpf_professor = str(i[3])
        cpf_aluno = str(i[4])
        arquivo.write("{} {} {} {} {}".format(cod_turma, periodo, cod_disciplina, cpf_professor, cpf_aluno))
    arquivo.close()



#PARA CADASTRO DE TURMA

def cadastro_turma(): #Função para pedir as informações da turma
    cod_turma = input("Para cadastrar a turma, digite o código dela: ")
    periodo = input("Digite o período da turma: ")
    cod_disciplina = input("Digite o código da disciplina: ")
    cpf_professor = input("Digite o CPF do professor: ")
    while True:
        cpf_aluno = input("Digite o CPF do aluno(para finalizar, digite 0): ")
        if cpf_aluno == '0':
            turma.append([cod_turma, periodo, cod_disciplina, cpf_professor, cpfs])
            salvar_turma()
            print('Turma cadastrada')
            break
        elif cpf_aluno in cpfs:
            print('Aluno já está nessa turma')
        else:
            cpfs.append(cpf_aluno)
            salvar_turma()
            print('Aluno adicionado')


#PARA REMOVER TURMA
def remover_turma():
    while True:
        try:
            op = int(input("Para remover turma digite 1\nPara retornar ao menu principal digite 2: "))
            if op == 1:
                del_turma = input("Digite o código da turma para prosseguir com a remoção: ")
                for i in range(len(turma)):
                    if del_turma in turma[i][0]:
                        print("CÓDIGO DA TURMA: {}\n"
                              "PERÍDODO: {}\n"
                              "CÓDIGO DA DISCIPLINA: {}\n"
                              "CPF PROFESSOR\n"
                              "CPF ALUNO: {}".format(turma[i][0], turma[i][1], turma[i][2], turma[i][3], turma[i][4]))
                        print("Turma removida com sucesso.")
                        turma.remove(turma[i])
                        salvar_turma()
                        break
                else:
                    print("Turma não cadastrada.")
            elif op == 2:
                break
            else:
                print("Operação inválida.")
        except EOFError:
            break


#ALTERAR TURMA
def alterar_turma():
    while True:
        try:
            op = int(input("Para alterar o cadastro da turma digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                alt_turma = input("Digite o código da turma que deseja alterar: ")
                for i in range(len(turma)):
                    if alt_turma in turma[i][0]:
                        opc = int(input("Para alterar o código da turma digite 1\n"
                                "Para alterar o período da turma digite 2\n"
                                "Para alterar o código da disciplina digite 3\n"
                                "Para alterar o CPF do professor digite 4\n"
                                "Para alterar o CPF do aluno cadastrado na turma digite 5\n"
                                "Digite a operação que deseja realizar: "))
                        if opc == 1:
                            cod = input("Digite o novo código da turma: ")
                            turma[i][0] = cod
                            salvar_turma()
                            print("CÓDIGO DA TURMA: {}\n"
                              "PERÍODO: {}\n"
                              "CÓDIGO DA DISCIPLINA: {}\n"
                              "CPF DO PROFESSOR: {}\n"
                              "CPF DO ALUNO: {}"
                              "Turma alterada com sucesso".format(turma[i][0], turma[i][1], turma[i][2], turma[i][3], turma[i][4]))
                            break
                        elif opc == 2:
                            periodo = input("Digite o novo período da turma:  ")
                            turma[i][1] = periodo
                            salvar_turma()
                            print("CÓDIGO DA TURMA: {}\n"
                              "PERÍODO: {}\n"
                              "CÓDIGO DA DISCIPLINA: {}\n"
                              "CPF DO PROFESSOR: {}\n"
                              "CPF DO ALUNO: {}"
                              "Turma alterada com sucesso.".format(turma[i][0], turma[i][1], turma[i][2], turma[i][3], turma[i][4]))
                            break
                        elif op == 3:
                            cod_d = input("Digite o novo código da disciplina: ")
                            turma[i][2] = cod_d
                            salvar_turma()
                            print("CÓDIGO DA TURMA: {}\n"
                              "PERÍODO: {}\n"
                              "CÓDIGO DA DISCIPLINA: {}\n"
                              "CPF DO PROFESSOR: {}\n"
                              "CPF DO ALUNO: {}"
                              "Turma alterada com sucesso.".format(turma[i][0], turma[i][1], turma[i][2], turma[i][3], turma[i][4]))
                            break
                        elif op == 4:
                            cpf_p = input("Digite o novo cpf do professor: ")
                            turma[i][3] == cod_p
                            salvar_turma()
                            print("CÓDIGO DA TURMA: {}\n"
                              "PERÍODO: {}\n"
                              "CÓDIGO DA DISCIPLINA: {}\n"
                              "CPF DO PROFESSOR: {}\n"
                              "CPF DO ALUNO: {}"
                              "Turma alterada com sucesso.".format(turma[i][0], turma[i][1], turma[i][2], turma[i][3], turma[i][4]))
                            break
                        elif op == 5:
                            while True:
                                cpf_a = input("Digite o novo cpf do aluno, caso deseje encerrar digite 0: ")
                                if cpd_a != "0":
                                    cpfs.append(cpf_a)
                                elif cpf_a == "0":
                                    turma[i][4] = cpfs
                                    salvar_turma()
                                    print("CÓDIGO DA TURMA: {}\n"
                                      "PERÍODO: {}\n"
                                      "CÓDIGO DA DISCIPLINA: {}\n"
                                      "CPF DO PROFESSOR: {}\n"
                                      "CPF DO ALUNO: {}"
                                      "Turma alterada com sucesso.".format(tuma[i][0], turma[i][1], turma[i][2], turma[i][3], turma[i][4]))
                                    break
                        else:
                            print("Operação inválida.")
                else:
                    print("Turma não cadastrada.")
            elif op == 2:
                break
            else:
                print("Operação inválida.")
        except EOFError:
            break


#PARA CONSULTAR TURMA
def consultar_turma():
    while True:
        try:
            op = int(input("Para consultar o cadastro da turma digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                consult_turma = input("Para consultar uma turma, digite o código dela: ")
                for i in range(len(turma)):
                    if consult_turma in turma[i][0]:
                        print("CÓDIGO DA TURMA: {}\n"
                                "PERÍODO: {}\n"
                                "CÓDIGO DA DISCIPLINA: {}\n"
                                "CPF DO PROFESSOR: {}\n"
                                "CPF DO ALUNO: {}".format(turma[i][0], turma[i][1], turma[i][2], turma[i][3], turma[i][4]))
                        break
                else:
                    print("Turma não cadastrada.")
            elif op == 2:
                break
            else:
                print("Operação inválida.")
        except EOFError:
            break
