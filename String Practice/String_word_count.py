n = 'Coffins with the remains of 19 Bosniaks found in mass graves and identified recently through DNA tests, have been buried Sunday in the memorial cemetery for victims of the genocide on the edge of the eastern Bosnian town.'
m = 'with'
count = 0
index = 0
sl = 0
for x in m:
    sl += 1

for i in n:
    if i == m[index]:
        index += 1
    else:
        index = 0
    if index == sl:
        count += 1;
        index = 0
print(count)
