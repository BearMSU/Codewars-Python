def calculate_years(principal, interest, tax, desired):
    year = 0
    
    while principal < desired:
        interest_earned = principal * interest
        after_tax_interest = interest_earned * (1 - tax)
        principal += after_tax_interest
        year += 1
        
    return year
​