#tupla que contém os contatos suportados pelo sistema
contatos_suportados = ("telefone", "email", "endereco")

#dicionario de exemplo
agenda = {
    "pessoa1":{
        "telefone":["11 99999-9999"],
        "email":["arthursgarbi037@gmail.com", "email.comercial@email.com"],
        "endereco":["rua python"]
    },
    "pessoa2":{
        "telefone":["11 98888-9999"],
        "email":["exemplo@email.com"],
        "endereco":["rua fim"]
    }
}

"""A função recebe um nome  de contato com str e um dicionario 
com as formas de contato, assim retornando uma str com os dados recebidos"""
def contato_txt(nome_contato:str, **formas_contato):
    formato_texto = f"{nome_contato}"
    for meio_contato, contato in formas_contato.items():
        formato_texto = f"{formato_texto}\n{meio_contato.upper()}"
        contador_formas = 1
        for valor in contato:
            formato_texto = f"{formato_texto}\n\t{contador_formas} - {valor.upper()}"
            contador_formas = contador_formas + 1

    return formato_texto

#teste
print(contato_txt("pessoa1", **agenda["pessoa1"]))

#função de ver toda a agenda utilizando a outra função
def agenda_txt(**agenda_completa):
    formato_texto = ""
    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto} {contato_txt(nome_contato, **formas_contato)}\n"
        formas_contato = f"{formato_texto}"
        formato_texto += "---------------------------------------------------\n"
    return formato_texto

#teste
print(agenda_txt(**agenda))

"""Agora vamos ver as funções que são necessárias para fazer 
alguma alteração na agenda como o nome que seria a chave e o 
número/email/endereço que seria os valores do dicionário"""

#função para alterar o nome
def altera_nome(agenda_original:dict, nome_original:str, nome_atualizado:str):
    if nome_original in agenda_original.keys():
        copia_contatos = agenda_original[nome_original].copy()
        agenda_original.pop(nome_original)
        agenda_original[nome_atualizado] = copia_contatos
        return True
    return False

#teste
altera_nome(agenda, "pessoa2", "Super pessoa")
print(agenda_txt(**agenda))

#função que altera a forma do contato
def altera_forma(lista_contato:list, antigo:str, novo:str):
    if antigo in lista_contato:
        posicao_antigo = lista_contato.index(antigo)
        lista_contato.pop(posicao_antigo)
        lista_contato.insert(posicao_antigo, novo)
        return True
    return False

altera_forma(agenda["pessoa1"]["telefone"], "11 99999-9999", "11 98765-4321")
print(agenda_txt(**agenda))

"""A partir daqui as funções são para excluir contatos
ou incluir contatos e suas formas de se comunicar!"""

#função para excluir um contato
def exclui_contato(agenda:dict, nome_contato:str):
    if nome_contato in agenda.keys():
        agenda.pop(nome_contato)
        return True
    return False

#teste
exclui_contato(agenda, "Super pessoa")
print(agenda_txt(**agenda))

#função de incluir contato
def inclui_contato(agenda:dict, nome_contato:str, **formas_contato):
    agenda[nome_contato] = formas_contato

#teste
inclui_contato(agenda, "Anninha", telefone=["11 98768-9442"], email=["a@b.com"])
print(agenda_txt(**agenda))

def inclui_forma_contato(formas_contato:dict, forma_incluida:str, valor_incluido:str):
    if forma_incluida in formas_contato.keys():
        formas_contato[forma_incluida].append(valor_incluido)
        return True
    elif forma_incluida in contatos_suportados:
        formas_contato[forma_incluida] = [valor_incluido]
        return True
    return False

#teste
inclui_forma_contato(agenda["Anninha"], "endereco", "Rua das Polianas")
print(agenda_txt(**agenda))

"""Agora aqui vem as interações com o usuário para que 
ele possa guardar as informações dos contatos e que ele 
possa escolher o que fazer sem ser de forma automatica pelo python."""

#função de incluir contato
def usuario_inclui_contato(agenda:dict):
    nome = input("Informe o novo nome do novo contato que será inserido na agenda: ")
    dicionario_formas = {}
    for forma in contatos_suportados:
        resposta = input(f"Deseja inserir um {forma} para {nome.upper()}? \nSIM ou NÃO -> ")
        lista_contatos = []
        while "S" in resposta.upper():
            lista_contatos.append(input(f"Informe um {forma}: "))
            resposta = input(f"Deseja inserir outro {forma} para {nome.upper()}? \nSIM ou NÃO -> ")
        if len(lista_contatos) > 0:
            dicionario_formas[forma] = lista_contatos.copy()
            lista_contatos.clear()
    if len(dicionario_formas.keys()) > 0:
        inclui_contato(agenda, nome, **dicionario_formas)
        print("Inclusão bem sucedida!!!")
    else:
        print("É necessário incluir pelo menos uma forma de contato! \nA agenda não foi alterada.")

#função de incluir uma forma de contato
def usuario_inclui_forma_contato(agenda:dict):
    nome = input("Informe o nome do contato que deseja incluir a forma de contato ")
    if nome in agenda.keys():
        print(f"As formas de contato suportadas pelo sistema são: {contatos_suportados}")
        forma_incluida = input("Qual a forma de contato deseja incluir? ")
        if forma_incluida in contatos_suportados:
            valor_incluido = input(f"Informe o {forma_incluida} que deseja incluir: ")
            if inclui_forma_contato(agenda[nome], forma_incluida, valor_incluido):
                print("Operação bem sucedida! A nova forma de contato foi incluída!!! ")
            else:
                print("Ocorreu um erro durante a inserção. A agenda não foi alterada.")
        else:
            print("A forma de contato indicada não é suportada pelo sistema. A agenda não foi alterada.")
    else:
        print("O contato informado não existe na agenda. Não foram feitas alterações. ")

#função de excluir contato
def usuario_exclui_contato(agenda:dict):
    nome = input("Informe o contato que deseja excluir: ")
    if exclui_contato(agenda, nome):
        print("Usuário excluido com sucesso!")
    else:
        print("Nome de usuário não encontrado. Não foram feitas alterações")

#função que altera contato
def usuario_altera_nome_contato(agenda:dict):
    nome_original = input("Informe o nome do contato que deseja alterar: ")
    nome_atualizado = input("Informe o nome que deseja colocar: ")
    if altera_nome(agenda, nome_original, nome_atualizado):
        print(f"O contato foi atualizado para {nome_atualizado}!")
    else:
        print(f"O contato original não foi localizado. A agenda não foi alterada.")

