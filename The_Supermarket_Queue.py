def queue_time(customers, n):
    d = {}
    
    if (not customers):
        return 0
    
    if n > sum(customers): 
        return max(customers)
    
    for i in range(n):
        d[i] = customers[i]
    
    for i in range(n, len(customers)):
        d[min(d, key = d.get)] += customers[i]
    return max(d.values())
