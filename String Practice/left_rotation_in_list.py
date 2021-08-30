def left_rotation(l, n):
    for i in range(n):
        t = l[0]
        for j in range(len(l) - 1):
            l[j] = l[j + 1]
        l[len(l) - 1] = t
    return l


l = [100, 200, 300, 400, 500, 600]
n = 2
print(left_rotation(l, n))
