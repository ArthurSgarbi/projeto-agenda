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

#função de ver toda a agenda
def agenda_txt(**agenda_completa):
    formato_texto = ""
    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto} {contato_txt(nome_contato, **formas_contato)}\n"
        formas_contato = f"{formato_texto}---------------------------------------------------\n"
    return formato_texto

#teste
print(agenda_txt(**agenda))
