def prem(nb):
    premier = True
    for i in range(2,nb):
        if nb/i == int(nb/i):
            premier = False    
    return premier