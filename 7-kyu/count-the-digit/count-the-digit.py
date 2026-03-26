def nb_dig(n, d):
    string_d = str(d)
    total_count = 0
    
    for k in range(n + 1):
        total_count += str(k**2).count(string_d)
    
    return total_count