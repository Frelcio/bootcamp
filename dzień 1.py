# imie = input('Podaj imię ')
# wiek = int(input('Podaj wiek '))
# wzrost = float(input('Podaj wzrost w metrach '))
# czy_uczysz = bool(int(input("Czy uczysz się Pythona? Podaj 1 dla tak, 0 dla nie. ")))
#
# print(f'Imię: {imie}\nWiek: {wiek}\nWzrost: {wzrost}\nCzy się uczy? {czy_uczysz}')
#
# s= 'abcdef'
# print((len(s)))
#
# print(s[len(s)-1])
# print(s[-1])
# print(s[2:4])
# print(s[2:])
# print(s[::2])
# print(s[::-1])
#
# s = '  a b c d e '
# print(s.upper())
# print(s.replace('a', 'x'))
# print(s.find('b'))
# print(s.count(' '))
# print(s.strip())
# print(s.strip().capitalize())
# print(s.strip().capitalize().startswith('A'))
#
# s = """
#  os. Jana III sobieskiego
# ul. Jana III Sobieskiego
# ul Jana      III Sobieskiego
#   ul.Jana III Sobieskiego
# ulicaJana III Sobieskiego
# Ul. Jana III Sobieskiego
# UL. Jana III     sobieskiego
#  ulica Jana Iii Sobieskiego
# Ulica. Jana      Ill Sobieskiego
# """
#
#
# t = s.upper().replace('   ', '').strip().replace('  ', '').replace('OS', 'UL').replace('ULICA', 'UL').replace('UL ', 'UL.').replace(' UL', 'UL').replace('UL.J', 'UL. J').replace('ULJ', 'UL. J').replace('ILL','III')
#
# t_list=(t.split('\n'))
# print(t_list)
# print(type(t.split('\n')))
# print(', '.join(t_list))
#
# print(s.split())
# print(' '.join(s.split()))

# l1 = float(input('Podaj pierwszą liczbę '))
# l2 = float(input('Podaj drugą liczbę '))
# l3 = float(input('Podaj trzecią liczbę '))
#
# l = []
# l.append(l1)
# l.append(l2)
# l.append(l3)
# l.sort()
# print(l)
# print(sum(l))

# s = {1 , 3, 5}
# print(s)
# print(len(s))
# print(max(s))
#
# s1 = {1, 2, 3}
# s2 = {1, "abc"}
# print(s1-s2)
# print(s1.intersection(s2))
# s1.add('def')
# print(s1)
# s1.pop()
# print(s1)
# print(s1.issubset(s2))
#
# print(list(s1))

# word = 'zzzzzzzzaabbb'
# if len(word) < 10:
#     print('krótkie słowo')
# elif len(word) >= 10:
#     if len(word)%13 == 0:
#         print('pechowe słowo')
#     elif word.count('a') >= 3:
#         print('aaa')
#     else:
#         print('długie słowo')

#
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# i = 0
# while i <= 30:
#     print(i)
#     if i < 10:
#         i += 5
#     else:
#         i += 10

# print()
# for i in [1, 3, 4]:
#     print(i)
#
# for i in {23, 34, 14, 33}:
#     if i % 3 == 0:
#         print(f'{i} jest podzioelna przez 3')
#     else:
#         print(i)

# for i in range(1, 100, 5):
#     print(i)

# c = 0
# for i in range(1_000_000):
#     if i % 5 == 0:
#         print(i)
#         c += 1
#     if c == 5:
#         break

for i in range(10):
    if i%2 == 0:
        print(f'{i} jest podzielna przez 2')
        continue
    print(i)
#
# for i in [1, 3, 4]
#     pass

# for i in [3, 5, 7]:
#     for j in [-1, -3, 4]:
#         ij = i*j
#         print(f'{i}*{j} = {ij}')
#
# for i, j in zip([1, 3, 4], [2, 3, 4]):
#     ij = i + j
#     print(f'{i}+{j}={ij}')
#
# for idx, i in enumerate(['raz', 'dwa', 'trzy']):
#     print(f'{idx}: {i}')


# s = 'kajak'
# for i in range(len(s)//2):
#     print(s[i])
#     print(s[-1-i])

# def len_diag(x1, x2):
#     return ((x1**2 + x2**2) **(1/2))
#
# print(len_diag(3,4))
