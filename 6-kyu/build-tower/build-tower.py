def tower_builder(n_floors):
    # build here
    tower = []
    width = (n_floors * 2) - 1
    
    for i in range (1, n_floors + 1):
        num_stars = (2 * i) - 1
        stars = "*" * num_stars
    
        num_spaces = (width - num_stars) // 2
        spaces = " " * num_spaces
    
        tower.append(f"{spaces}{stars}{spaces}")
    return tower