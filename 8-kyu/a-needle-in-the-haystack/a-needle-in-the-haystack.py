def find_needle(haystack):
    # your code here
    for i, junk in enumerate(haystack):
        if junk == "needle":
            return f"found the needle at position {i}"