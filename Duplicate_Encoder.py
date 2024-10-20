def duplicate_encode(word):
    word = word.lower()
    
    resultado = ""
    
    for letra in word:
        
        if word.count(letra) > 1:
            resultado += ")"
        else:
            resultado += "("
    
    return resultado
