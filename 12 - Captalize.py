def capitalize(string):
    st = string[0].upper()
    for c in range(1, len(string)):
        if string[c-1] == " " and string[c].isalpha():
            st = st + string[c].upper()
        else:
            st = st + string[c]
    return st