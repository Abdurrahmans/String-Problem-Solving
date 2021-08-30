string = "AbdurRahMaN"
lower = []
upper = []
for char in string:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
res = ''.join(lower + upper)
print(res)
