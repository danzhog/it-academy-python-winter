# Посчитать количество строчных (маленьких)
# и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

s1 = str(input('введите строку: '))

UP = 0
low = 0

for i in s1:
    if 'a' <= i <= 'z':
        low += 1
    elif 'A' <= i <= 'Z':
        UP += 1

print('количество строчных букв в строке:', low)
print('количество прописных букв в строке:', UP)
