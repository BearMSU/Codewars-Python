import re
def validate_pin(pin):
    # return true or false
    pattern = r"^(\d{4}|\d{6})$"
    
    if re.fullmatch(pattern, pin):
        return True
    else:
        return False