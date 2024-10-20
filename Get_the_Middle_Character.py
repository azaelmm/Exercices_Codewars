def get_middle(s):
    
    caracterDelMedio = ""
    
    if (len(s)%2 != 0):
        caracterDelMedio = s[(len(s)-(len(s)//2))-1:len(s)-(len(s)//2)]
    else:
        caracterDelMedio = s[(len(s)-(len(s)//2))-1:(len(s)-(len(s)//2))+1]
    return caracterDelMedio
