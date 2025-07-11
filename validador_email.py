#Esse é um script de uma função para validar email

#email = input().strip() ---> Essa linha deve ser transformada ao normal depois dos testes

def validar_email(email):
    email = email.strip()

    if email.count("@") != 1:
        return "E-mail inválido"
    
    if " " in email:
        return "E-mail inválido"
    
    if email.startswith("@") or email.endswith("@"):
        return "E-mail inválido"
    
    nome_usuario, dominio = email.split("@")
    
    if "." not in dominio:
        return "E-mail inválido"
    
    return "E-mail válido"