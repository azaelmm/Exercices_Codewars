def friend(x):
    
    listFriends = []
    
    for name in x:
        if len(name) == 4:
            listFriends.append(name)
        
    return listFriends
