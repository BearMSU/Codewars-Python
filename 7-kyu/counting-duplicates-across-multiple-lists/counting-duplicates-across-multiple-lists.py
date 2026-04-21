def count_duplicates(name,age,height):
    # your code here
    entry_counts = {}
    
    for entry in zip(name, age, height):
        if entry in entry_counts:
            entry_counts[entry] += 1
        else:
            entry_counts[entry] = 1
    
    total_duplicates = 0
    
    for count in entry_counts.values():
        if count > 1:
            total_duplicates += (count - 1)
    return total_duplicates
    
    