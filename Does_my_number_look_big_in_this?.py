def narcissistic( value ):
    
    lista_separada = list(str(value))
    
    longitud = len(lista_separada)
    
    suma = 0
    
    for numero in lista_separada:
        
        digito = int(numero)
        
        potencia = digito ** longitud
        
        suma += potencia
        
    if suma == value:
        return True
    else:
        return False
