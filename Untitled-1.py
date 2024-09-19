mez = int(input("Zadej vrchní mez: "))

i = 2
seznam = []
for x in range(2, mez+1):
     seznam.append(x)


while i * i <= mez:
    if seznam[i]:
        j = i - 2
        while j < mez - i - 1:
            j += i
            seznam[int(j)] = False
    i += 1


for index, value in enumerate(seznam):
    if value:
        print(f"{value}")