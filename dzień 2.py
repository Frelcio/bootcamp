# #
# # l = list(range(0, 101, 2))
# # for i in range(len(l)):
# #     if l[i] % 3 == 0:
# #         l[i] *= 100
# #
# # print(l)
#
# s = 'Python jest moim ulubionym językiem programowania'
# s_list = s.split(' ')
#
#
# res = []
# for i in s_list:
#     i_len = len(i)
#     res.append(i_len)
# print(s_list)
# print(res)
#
# print([len(i) for i in s_list])
#
# print({len(i) for i in s_list})
#
# print([(i, len(i)) for i in s_list])
#
# print({i: len(i) for i in s_list})
#
# DATA = [
#     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
#     (5.8, 2.7, 5.1, 1.9, 'virginica'),
#     (5.1, 3.5, 1.4, 0.2, 'setosa'),
#     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
#     (6.3, 2.9, 5.6, 1.8, 'virginica'),
#     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
#     (4.7, 3.2, 1.3, 0.2, 'setosa'),
#     (7.0, 3.2, 4.7, 1.4, 'versicolor')]
#
# # for i in DATA:
# #     print(i[4])
#
# print({i[4] for i in DATA[1:]})
# print(max([i[2] for i in DATA[1:]]))
#
# s = 'Python jest moim ulubionym językiem programowania'
# s_list = s.split(' ')
#
#
# res = []
# for i in s_list:
#     i_len = len(i)
#     if i_len > 6:
#         res.append(i_len)
# print(s_list)
# print(res)
#
# print(min([i[2] for i in DATA[1:] if i[-1] == 'setosa']))
#
# print(min([i[2] for i in DATA[1:] if i[-1] == 'setosa']))
#
# def l_stats(l):
#     l_max = max(l)
#     l_min = min(l)
#     l_len = len(l)
#     l_mean = sum(l)/l_len
#     return (l_max, l_min, l_len, l_mean)
#
# print(l_stats([-2,3,5,7]))
#
# a, b, c, d = l_stats([-2,3,5,7])
# print(a, b, c, d)
#
# a, b, c, _ = l_stats([-2,3,5,7])
#
# print(_)
#
# l = [1, 3, 'x'],
#
# print(sum(list(map(lambda x: x % 2, list(range(1, 101))))))
#
# print('fibonacci')
#
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(13))


def check(t):
    if type(t) not in {float, int}:
        raise TypeError('temperatura musi być liczbą')
    if t < 0:
        raise   ValueError("temp w kelvinach nie może być ujemna")
    return t

check(10)

def check_age(t):
    if type(t) != int:
        raise TypeError('wiek musi być liczbą całkowitą')
    if t < 0:
        raise   ValueError("wiek nie może być ujemny")
    return t

check_age(50.5)

try