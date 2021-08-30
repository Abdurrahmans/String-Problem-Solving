def appendMiddle(s1, s2):
    mid = int(len(s1) / 2)
    append_middle = s1[:mid] + s2 + s1[mid:]
    print("Middle Three Char:", append_middle)


appendMiddle("Ault", "Kelly")
