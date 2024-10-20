def create_phone_number(n):
    lista_de_digitos = []
    
    for i in n:
        lista_de_digitos.append(str(i))
    
    cadena_digitos = "".join(lista_de_digitos)
    
    codigo_area = cadena_digitos[0:3]
    primera_parte = cadena_digitos[3:6]
    segunda_parte = cadena_digitos[6:]
    
    numero_telefono = "(" + codigo_area + ") " + primera_parte + "-" + segunda_parte
    
    return numero_telefono
