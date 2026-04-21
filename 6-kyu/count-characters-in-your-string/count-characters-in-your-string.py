def count(s):
    # if string is empty: return {}
    s_dict = {}
    if s == '':
        return {}
    else:
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
    return s_dict
​