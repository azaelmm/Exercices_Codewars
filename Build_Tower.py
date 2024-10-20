def tower_builder(n_floors):
    torre = []
    floor = ''

    for f in range(n_floors):
        
        # Calcular el número de asteriscos para el piso actual
        num_asteriscos = f * 2 + 1 # Esto asegura que el número de asteriscos sea impar
        
        stars = ''
        for x in range(num_asteriscos):
            stars += '*'  
        
        # Calcular el número de espacios para el piso actual
        num_espacios = n_floors - f - 1
        spaces = ''
        for _ in range(num_espacios):
            spaces += ' ' 

        floor = spaces + stars + spaces
        torre.append(floor)
        
    return torre
