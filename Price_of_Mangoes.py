def mango(quantity, price):
    
    res = 0
    
    if (quantity >= 3 ):
        res = ((quantity - (quantity//3)) * price)
    else:
        res = quantity * price
    return res
