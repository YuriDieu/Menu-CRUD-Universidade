#Yuri Matheus Dieudonné Psybiowski da Silva
#Disciplina de Raciocínio Computacional
#Inteligência Artificial Aplicada
#Atividade Somativa 2

import json #Importação da biblioteca JSON

lista_de_estudantes = [] #Declaração da lista
opcao_1 = 1

#criação de uma função para que não seja colocado o menu em todo o código.
'''A função é criada do chamamento "def" e o respectivo "nome", juntamente com os ()'''
def menu_opcoes_geral():
    print("Bem-vindo ao MENU PRINCIPAL! Digite uma opção válida e aperte ENTER no final.\n")
    print("1 - Gerenciar ESTUDANTES\n")
    print("2 - Gerenciar PROFESSORES\n")
    print("3 - Gerenciar DISCIPLINAS\n")
    print("4 - Gerenciar TURMAS\n")
    print("5 - Gerenciar MATRÍCULAS\n")
    print("0 - SAIR\n")
    return int(input("Qual é a sua opção?  "))

#Criação de um submenu
def submenu():
    print("1 - LISTAR")
    print("2 - INCLUIR")
    print("3 - ALTERAR")
    print("4 - EXCLUIR")
    print("0 - SAIR")
    return int(input("Digite o número referente ao MENU acima: "))

#Aqui tenho que listar os estudantes que foram incluídos
def listagem_estudantes():
    
    print("\nVocê escolheu a opção LISTAR")
    
    #Agora vou listar o dicionário salvo no arquivo
    data = recuperar_arquivo_estudantes()
    if len(data) < 1:
        print("\n**Não há estudantes cadastrados.**")
    for i in data:
        print("\nCódigo do estudante: {}".format(i["código"]))
        print("Nome do estudante: {}".format(i["nome"]))
        print("CPF do estudante: {}".format(i["CPF"]))
            

#Aqui tenho que incluir o/a(s) estudante(s)
def inclusao_dados_estudantes():
    
    print("\nVocê escolheu a opção INCLUIR")
    
    #Abaixo será realizado a entrada de dados dos estudantes
    cod_estudante = int(input("\nInforme o código do estudante e aperte ENTER: "))
    nome_estudante = input("\nInforme o nome do estudante e aperte ENTER: ")
    CPF_estudante = input("\nDigite o CPF do estudante e aperte ENTER: ")
    dic_estudantes = {
        "código": cod_estudante,
        "nome": nome_estudante,
        "CPF": CPF_estudante
    }
    #lista_de_estudantes.append(dic_estudantes)
    #Abaixo vou fazer a tentativa de incluir arquivos JSON
    #Adiciona o dicionário no arquivo
    data = recuperar_arquivo_estudantes()
    data.append(dic_estudantes)
    salvar_arquivo_estudantes(data)

#Aqui eu tenho que alterar os dados dos alunos cadastrados
def alterar_dados_estudantes():
    
    print("\nVocê escolheu a opção ALTERAR")
    
    data = recuperar_arquivo_estudantes()
    seg = False
    search_cod = int(input("\nDigite o CÓDIGO do estudante que queira ALTERAR os dados: "))
    for i in data:
        if i["código"] == search_cod:
            print("\nEstudante encontrado!")
            print("Aletere o(s) dado(s) que desejar: ")
            cod_estudante = int(input("\nInforme o código do estudante e aperte ENTER: "))
            nome_estudante = input("\nInforme o nome do estudante e aperte ENTER: ")
            CPF_estudante = input("\nDigite o CPF do estudante e aperte ENTER: ")
            i["código"]= cod_estudante
            i["nome"] = nome_estudante
            i["CPF"] = CPF_estudante
            seg = True
            break
    if not seg:
        print("\nEstudante não encontrado!")
    else:
        #Aqui ele salva os dados alterados no arquivo
        salvar_arquivo_estudantes(data)
        
#Função de exclusão de dados
def exclusao_dados_estudantes():
    
    print("\nVocê escolheu a opção EXCLUIR")
    
    data = recuperar_arquivo_estudantes() #Isso é uma função dentro de outra função!
    seg = False
    search_cod = int(input("\nDigite o CÓDIGO do estudante que queira EXCLUIR os dados: "))
    for i in data:
        if i["código"] == search_cod:
            print("\nEstudante encontrado!\nSeus dados foram excluídos.")
            data.remove(i)
            seg = True
            break
    if not seg:
        print("\nEstudante não encontrado!")
    else:
        #Aqui ele salva os dados alterados no arquivo
        salvar_arquivo_estudantes(data) #Isso é uma função dentro da função!
        
#Função de recuperação de arquivo
def recuperar_arquivo_estudantes():
    try:
        with open("estudantes.json", "r") as f: #Aqui abre o arquivo "estudantes.json" para leitura
            data = json.load(f)                 #e o chama de "f", então cria-se o objeto "data" que
    except FileNotFoundError:                   #recebe o load do arquivo "f", ou seja, carrega o arquivo "estudantes.json"
            data = []
    return data

#Função para salvar arquivos
def salvar_arquivo_estudantes(data):
    with open("estudantes.json", "w") as f: #Aqui abre o arquivo para escrita
        json.dump(data, f) #Converte a lista com o dicionário na string JSON e grava os dados no arquivo

#Função listar para professores
def listagem_professores():
    
    print("\nVocê escolheu a opção LISTAR")
    
    data = recuperar_arquivo_professores()
    if len(data) < 1:
        print("\n**Não há professores cadastrados.**")
    for i in data:
        print("\nCódigo do professor: {}".format(i["código"]))
        print("Nome do professor: {}".format(i["nome"]))
        print("CPF do professor: {}".format(i["CPF"]))

def inclusao_dados_professores():
    
    print("\nVocê escolheu a opção INCLUIR")
    
    #Abaixo será realizado a entrada de dados dos professores
    cod_professor = int(input("\nInforme o código do professor e aperte ENTER: "))
    nome_professor = input("\nInforme o nome do professor e aperte ENTER: ")
    CPF_professor = input("\nDigite o CPF do professor e aperte ENTER: ")
    dic_professores = {
        "código": cod_professor,
        "nome": nome_professor,
        "CPF": CPF_professor
    }
    data = recuperar_arquivo_professores()
    data.append(dic_professores)
    salvar_arquivo_professores(data)
    '''Tenho que alterar o arquivo json, pois se eu usar o dos estudantes, ficará salvo lá'''

#Aqui será alterado os dados dos professores
def alterar_dados_professores():
    
    print("\nVocê escolheu a opção ALTERAR")
    
    data = recuperar_arquivo_professores()
    seg = False
    search_cod = int(input("\nDigite o CÓDIGO do professor que queira ALTERAR os dados: "))
    for i in data:
        if i["código"] == search_cod:
            print("\nProfessor encontrado!")
            print("Aletere o(s) dado(s) que desejar: ")
            cod_professor = int(input("\nInforme o código do estudante e aperte ENTER: "))
            nome_professor = input("\nInforme o nome do estudante e aperte ENTER: ")
            CPF_professor = input("\nDigite o CPF do estudante e aperte ENTER: ")
            i["código"]= cod_professor
            i["nome"] = nome_professor
            i["CPF"] = CPF_professor
            seg = True
            break
    if not seg:
        print("\nProfessor não encontrado!")
    else:
        salvar_arquivo_professores(data)

def exclusao_dados_professores():
    
    print("\nVocê escolheu a opção EXCLUIR")
    
    data = recuperar_arquivo_professores()
    seg = False
    search_cod = int(input("\nDigite o CÓDIGO do professor que queira EXCLUIR os dados: "))
    for i in data:
        if i["código"] == search_cod:
            print("\nProfessor encontrado!\nSeus dados foram excluídos.")
            data.remove(i)
            seg = True
            break
    if not seg:
        print("\nProfessor não encontrado!")
    else:
        salvar_arquivo_professores(data)

#Função de recuperação de arquivo
def recuperar_arquivo_professores():
    try:
        with open("professores.json", "r") as f: #Aqui abre o arquivo "professores.json" para leitura
            data = json.load(f)                 #e o chama de "f", então cria-se o objeto "data" que
    except FileNotFoundError:                   #recebe o load do arquivo "f", ou seja, carrega o arquivo "professores.json"
            data = []
    return data

#Função para salvar arquivos
def salvar_arquivo_professores(data):
    with open("professores.json", "w") as f:
        json.dump(data, f)

def listagem_disciplinas():
    
    print("\nVocê escolheu a opção LISTAR")
    
    data = recuperar_arquivo_disciplinas()
    if len(data) < 1:
        print("\n**Não há disciplinas cadastradas.**")
    for i in data:
        print("\nCódigo da disciplina: {}".format(i["código"]))
        print("Nome da disciplina: {}".format(i["nome"]))

def inclusao_dados_disciplinas():
    
    print("\nVocê escolheu a opção INCLUIR")
    
    #Abaixo será realizado a entrada de dados das disciplinas
    cod_disciplina = int(input("\nInforme o código da disciplina e aperte ENTER: "))
    nome_disciplina = input("\nInforme o nome da disciplina e aperte ENTER: ")
    dic_disciplinas = {
        "código": cod_disciplina,
        "nome": nome_disciplina,
    }
    data = recuperar_arquivo_disciplinas()
    data.append(dic_disciplinas)
    salvar_arquivo_disciplinas(data)
    '''Tenho que alterar o arquivo json, pois se eu usar o dos estudantes, ficará salvo lá'''
    
def alterar_dados_disciplinas():
    
    print("\nVocê escolheu a opção ALTERAR")
    
    data = recuperar_arquivo_disciplinas()
    seg = False
    search_cod = int(input("\nDigite o CÓDIGO da disciplina que queira ALTERAR os dados: "))
    for i in data:
        if i["código"] == search_cod:
            print("\nDisciplina encontrada!")
            print("Aletere o(s) dado(s) que desejar: ")
            cod_disciplina = int(input("\nInforme o código da disciplina e aperte ENTER: "))
            nome_disciplina = input("\nInforme o nome da disciplina e aperte ENTER: ")
            i["código"]= cod_disciplina
            i["nome"] = nome_disciplina
            seg = True
            break
    if not seg:
        print("\nDisciplina não encontrada!")
    else:
        #Aqui ele salva os dados alterados no arquivo
        salvar_arquivo_disciplinas(data)

def exclusao_dados_disciplinas():
    
    print("\nVocê escolheu a opção EXCLUIR")
    
    data = recuperar_arquivo_disciplinas()
    seg = False
    search_cod = int(input("\nDigite o CÓDIGO da disciplina que queira EXCLUIR os dados: "))
    for i in data:
        if i["código"] == search_cod:
            print("\nDisciplina encontrada!\nSeus dados foram excluídos.")
            data.remove(i)
            seg = True
            break
    if not seg:
        print("\nDisciplina não encontrada!")
    else:
        #Aqui ele salva os dados alterados no arquivo
        salvar_arquivo_disciplinas(data)

#Função de recuperação de arquivo
def recuperar_arquivo_disciplinas():
    try:
        with open("disciplinas.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
            data = []
    return data

#Função para salvar arquivos
def salvar_arquivo_disciplinas(data):
    with open("disciplinas.json", "w") as f:
        json.dump(data, f)

def listagem_turmas():
    
    print("\nVocê escolheu a opção LISTAR")
    
    data = recuperar_arquivo_turmas()
    if len(data) < 1:
        print("\n**Não há turmas cadastradas.**")
    for i in data:
        print("\nCódigo da turma: {}".format(i["código"]))
        print("Código do professor: {}".format(i["código1"]))
        print("Código da disciplina: {}".format(i["código2"]))

def inclusao_dados_turmas():
    
    print("\nVocê escolheu a opção INCLUIR")
    
    #Abaixo será realizado a entrada de dados das turmas
    cod_turma = int(input("\nInforme o código da turma e aperte ENTER: "))
    cod_professor = int(input("\nInforme o código do professor e aperte ENTER: "))
    cod_disciplina = int(input("\nInforme o código da disciplina e aperte ENTER: "))
    dic_turmas = {
        "código": cod_turma,
        "código1": cod_professor,
        "código2": cod_disciplina,
    }
    
    data = recuperar_arquivo_turmas()
    data.append(dic_turmas)
    salvar_arquivo_turmas(data)
    
def alterar_dados_turmas():
    
    print("\nVocê escolheu a opção ALTERAR")
    
    data = recuperar_arquivo_turmas()
    seg = False
    search_cod = int(input("\nDigite o CÓDIGO da turma que queira ALTERAR os dados: "))
    for i in data:
        if i["código"] == search_cod:
            print("\nTurma encontrada!")
            print("Aletere o(s) dado(s) que desejar: ")
            cod_turma = int(input("\nInforme o código da turma e aperte ENTER: "))
            cod_professor = int(input("\nInforme o código do professor e aperte ENTER: "))
            cod_disciplina = int(input("\nInforme o código da disciplina e aperte ENTER: "))
            i["código"]= cod_turma
            i["código1"] = cod_professor
            i["código2"] = cod_disciplina
            seg = True
            break
    if not seg:
        print("\nTurma não encontrada!")
    else:
        #Aqui ele salva os dados alterados no arquivo
        salvar_arquivo_turmas(data)

def exclusao_dados_turmas():
    
    print("\nVocê escolheu a opção EXCLUIR")
    
    data = recuperar_arquivo_turmas()
    seg = False
    search_cod = int(input("\nDigite o CÓDIGO da turma que queira EXCLUIR os dados: "))
    for i in data:
        if i["código"] == search_cod:
            print("\nTurma encontrada!\nSeus dados foram excluídos.")
            data.remove(i)
            seg = True
            break
    if not seg:
        print("\nTurma não encontrada!")
    else:
        #Aqui ele salva os dados alterados no arquivo
        salvar_arquivo_turmas(data)

#Função de recuperação de arquivo
def recuperar_arquivo_turmas():
    try:
        with open("turmas.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
            data = []
    return data

#Função para salvar arquivos
def salvar_arquivo_turmas(data):
    with open("turmas.json", "w") as f: #Aqui abre o arquivo para escrita
        json.dump(data, f)

def listagem_matriculas():
    
    print("\nVocê escolheu a opção LISTAR")
    
    data = recuperar_arquivo_matriculas()
    if len(data) < 1:
        print("\n**Não há matrículas cadastradas.**")
    for i in data:
        print("\nCódigo da turma: {}".format(i["código"]))
        print("Código do estudante: {}".format(i["código1"]))

def inclusao_dados_matriculas():
    
    print("\nVocê escolheu a opção INCLUIR")
    
    cod_turma = int(input("\nInforme o código da turma e aperte ENTER: "))
    cod_estudante = int(input("\nInforme o código do estudante e aperte ENTER: "))
    dic_matriculas = {
        "código": cod_turma,
        "código1": cod_estudante,
    }
    
    data = recuperar_arquivo_matriculas()
    data.append(dic_matriculas)
    salvar_arquivo_matriculas(data)
    
def alterar_dados_matriculas():
    
    print("\nVocê escolheu a opção ALTERAR")
    
    data = recuperar_arquivo_matriculas()
    seg = False
    search_cod = int(input("\nDigite o CÓDIGO da matrícula que queira ALTERAR os dados: "))
    for i in data:
        if i["código"] == search_cod:
            print("\nMatrícula encontrada!")
            print("Aletere o(s) dado(s) que desejar: ")
            cod_turma = int(input("\nInforme o código da turma e aperte ENTER: "))
            cod_estudante = int(input("\nInforme o código do estudante e aperte ENTER: "))
            i["código"]= cod_turma
            i["código1"] = cod_estudante
            seg = True
            break
    if not seg:
        print("\nMatrícula não encontrada!")
    else:
        #Aqui ele salva os dados alterados no arquivo
        salvar_arquivo_matriculas(data)

def exclusao_dados_matriculas():
    
    print("\nVocê escolheu a opção EXCLUIR")
    
    data = recuperar_arquivo_matriculas()
    seg = False
    search_cod = int(input("\nDigite o CÓDIGO da matrícula que queira EXCLUIR os dados: "))
    for i in data:
        if i["código"] == search_cod:
            print("\nMatrícula encontrada!\nSeus dados foram excluídos.")
            data.remove(i)
            seg = True
            break
    if not seg:
        print("\nMatrícula não encontrada!")
    else:
        salvar_arquivo_matriculas(data)

#Função de recuperação de arquivo
def recuperar_arquivo_matriculas():
    try:
        with open("matriculas.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
            data = []
    return data

#Função para salvar arquivos
def salvar_arquivo_matriculas(data):
    with open("matriculas.json", "w") as f: #Aqui abre o arquivo para escrita
        json.dump(data, f)

while opcao_1 != 0:

    opcao_1 = menu_opcoes_geral()
    
    if opcao_1 == 1:
        
        opcao_2 = 1
        while opcao_2 != 0:

            print("\nGERENCIAMENTO DE ESTUDANTES\n")
            opcao_2 = submenu()
            
            #Abaixo faço o uso das funções criadas acima
            if opcao_2 == 1:
                listagem_estudantes()
            elif opcao_2 == 2:
                inclusao_dados_estudantes()
            elif opcao_2 == 3:
                alterar_dados_estudantes()
            elif opcao_2 == 4:
                exclusao_dados_estudantes()
            elif opcao_2 == 0:
                print("\nVocê escolheu a opção SAIR\n")
            else:
                print("\nA opção escolhida é inválida.")
                
    elif opcao_1 == 2:

        opcao_2 = 1        
        while opcao_2 != 0:

            print("\nGERENCIAMENTO DE PROFESSORES.\n")
            opcao_2 = submenu()
            
            if opcao_2 == 1:
                listagem_professores()
            elif opcao_2 == 2:
                inclusao_dados_professores()
            elif opcao_2 == 3:
                alterar_dados_professores()
            elif opcao_2 == 4:
                exclusao_dados_professores()
            elif opcao_2 == 0:
                print("\nVocê escolheu a opção SAIR")
            else:
                print("\nA opção escolhida é inválida.")
                
    elif opcao_1 == 3:
        
        opcao_2 = 1
        while opcao_2 != 0:
            
            print("\nGERENCIAMENTO DE DISCIPLINAS")
            opcao_2 = submenu()
         
            if opcao_2 == 1:
                listagem_disciplinas()
            elif opcao_2 == 2:
                inclusao_dados_disciplinas()
            elif opcao_2 == 3:
                alterar_dados_disciplinas()
            elif opcao_2 == 4:
                exclusao_dados_disciplinas()
            elif opcao_2 == 0:
                print("\nVocê escolheu a opção SAIR")
            else:
                print("\nA opção escolhida é inválida.")

    elif opcao_1 == 4:

        opcao_2 = 1
        while opcao_2 != 0:
            
            print("\nGERENCIAMENTO DE TURMAS")
            opcao_2 = submenu()
            
            if opcao_2 == 1:
                listagem_turmas()
            elif opcao_2 == 2:
                inclusao_dados_turmas()
            elif opcao_2 == 3:
                alterar_dados_turmas()
            elif opcao_2 == 4:
                exclusao_dados_turmas()
            elif opcao_2 == 0:
                print("\nVocê escolheu a opção SAIR")
            else:
                print("\nA opção escolhida é inválida.")
                
    elif opcao_1 == 5:
        
        opcao_2 = 1
        while opcao_2 != 0:
            
            print("\nGERENCIAMENTO DE MATRÍCULAS")
            
            opcao_2 = submenu()
            if opcao_2 == 1:
                listagem_matriculas()
            elif opcao_2 == 2:
                inclusao_dados_matriculas()
            elif opcao_2 == 3:
                alterar_dados_matriculas()
            elif opcao_2 == 4:
                exclusao_dados_matriculas()
            elif opcao_2 == 0:
                print("\nVocê escolheu a opção SAIR")
            else:
                print("\nA opção escolhida é inválida.")
    
    elif opcao_1 == 0:
        print("\nSAIR")
        print("\nFim do programa.")
    else:
        print("A opção escolhida é inválida. Tente novamente.")