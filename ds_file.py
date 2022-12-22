print('1 задание ----------------------------------------')
my_f1 = open('text1.txt')
my_f2 = open('text2.txt')
if my_f1.readlines() == my_f2.readlines():
    print('Строки этих файлов равны')
else:
    print('Строки этих файлов НЕ равны')
my_f1.close()
my_f2.close()

print('4 задание ----------------------------------------')
my_f = open('text5.txt')
plist = []
for i in my_f.readlines():
    plist.append(i)
print('Длина самой длинной строки =', len(max(plist)))
my_f.close()

import string
print('2 задание ----------------------------------------')
vowels = ['e', 'y', 'u', 'i', 'o', 'a']
sogl = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
vowels_counter = 0
sogl_counter = 0
digit_counter = 0
symbol_counter = 0
my_f1 = open('text3.txt')
plist = my_f1.readlines()
for i in plist:
    for j in i:
        if j in vowels:
            vowels_counter += 1
        elif j in sogl:
            sogl_counter += 1
        elif j in string.digits:
            digit_counter += 1
        symbol_counter += 1
my_f1.close()
my_f2 = open('text4.txt', 'w')
my_f2.write(f'количество символов в файле = {symbol_counter - len(plist) + 1}\n')
my_f2.write(f'количество строк в файле = {len(plist)}\n')
my_f2.write(f'количество гласных букв в файле = {vowels_counter}\n')
my_f2.write(f'количество согласных букв в файле = {sogl_counter}\n')
my_f2.write(f'количество цифр в файле = {digit_counter}\n')
my_f2.close()
