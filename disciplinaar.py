disciplina = []
#PARA SALVAR CADASTRO, ATUALIZAÇÃO E REMOÇÃO
def salvar_cadastrod():
    global disciplina
    arq = open('disciplinas.txt', 'w', encoding = "utf-8")
    for i in disciplina:
        nome_disciplina = str(i[0])
        cod_disciplina = str(i[1])
        arq.write('%s %s\n' % (nome_disciplina, cod_disciplina))
    arq.close()


#PARA O CADASTRO DE DISCIPLINA
def cadastro_disciplina():
    while True:
        try:
            op = int(input("Para realizar o cadastro de disciplina digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                nome_disciplina = input("Digite o nome da disciplina: ")
                cod_disciplina = input("Digite o código da disciplina: ")
                for i in range(len(disciplina)):
                    if cod_disciplina in disciplina[i][1]:
                        print("Disciplina já cadastrada.")
                        break
                else:
                    disciplina.append([nome_disciplina, cod_disciplina])
                    print("Disciplina cadastrada com sucesso.\n NOME DA DISCIPLINA: {}\nCÓDIGO DA DISCIPLINA: {}".format(nome_disciplina, cod_disciplina))
                    salvar_cadastrod()
            elif op == 2:
                break
            else:
                print("Operação inválida.")
        except EOFError:
            break


#PARA REMOÇÃO DE DISCIPLINA
def remover_disciplina():
    while True:
        try:
            op = int(input("Para remoção de disciplina digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                del_disciplina = input("Para remover disciplina, digite o código dela: ")
                for i in range(len(disciplina)):
                    if del_disciplina in disciplina[i][1]:
                        disciplina.remove(disciplina[i])
                        salvar_cadastrod()
                        print("Disciplina removida.")
                    else:
                        print("Cadastro não encontrado.")
            elif op == 2:
                break
            else:
                print("Operação inválida.")
        except EOFError:
            break



#PARA ALTERAR DISCIPLINA
def alterar_disciplina():
    while True:
        try:
            op = int(input("Para a atualização de disciplina, digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                alt_disciplina = input("Digite o código da disciplina para ter acesso à atualização: ")
                for i in range(len(disciplina)):
                    if alt_disciplina in disciplina[i][1]:
                        opc = int(input("Digite o que deseja atualizar(1 para NOME, 2 para CÓDIGO): "))
                        if opc == 1:
                            nome = input("Digite o novo nome da disciplina aqui: ")
                            disciplina[i][0] = nome
                            salvar_cadastrod()
                            print("NOME DA DISCIPLINA: {}, CÓDIGO DA DISCIPLINA: {}".format(disciplina[i][0], disciplina[i][1]))
                            print("Disciplina alterada com sucesso.")
                        elif opc == 2:
                            cod = input("Digite o novo código da disciplina: ")
                            disciplina[i][1] = cod
                            salvar_cadastrod()
                            print("NOME DA DISCIPLINA: {}\nCÓDIGO DA DISCIPLINA: {}".format(disciplina[i][0], disciplina[i][1]))
                            print("Disciplina alterada com sucesso.")
                    else:
                        print("Cadastro não encontrado.")
            elif op == 2:
                break
            else:
                print("Operação inválida.")
        except EOFError:
            break



#PARA CONSULTAR DISCIPLINA
def consultar_disciplina():
    while True:
        try:
            op = int(input("Para consultar o cadastro da disciplina digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                consult_disciplina = input("Para consulta, digite o código dela aqui: ")
                for i in range(len(disciplina)):
                    if consult_disciplina in disciplina[i][1]:
                        print("NOME DA DISCIPLINA: {}\nCÓDIGO DA DISCIPLINA: {}".format(disciplina[i][0], disciplina[i][1]))
                        break
                    else:
                        print("Cadastro não encontrado.")
            elif op == 2:
                break
            else:
                print("operação inválida.")
        except EOFError:
            break

