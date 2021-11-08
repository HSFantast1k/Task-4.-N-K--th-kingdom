import time
from itertools import combinations


def search_prime_list(min_number, max_number):
    prime_list = [2]
    for i in range(3, max_number + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in prime_list:
            if j * j - 1 > i:
                prime_list.append(i)
                break
            if (i % j == 0):
                break
        else:
            prime_list.append(i)
    return prime_list


# print([c for c in combinations(search_prime_list(30), 3)])

a = int(input()) #a и b диапазон N, где
b = int(input()) + 1 #N - кол-чи простых чисел для представление числа,
# сразу можна добавить +1 для удобней работы с функцыей range

c = int(input()) #с и d диапазон K, где
d = int(input()) + 1 #K - диапазон желаемых чисел,
# сразу можна добавить +1 для удобней работы с функцыей range


resualt_count = 0
resualt_set = set()
all_resualt = {}

for numbers in range(c, d):
    for N in range(a, b):
        resualt_combinations_list = [temp_list for temp_list in combinations(search_prime_list(c, d), N)]
        for temp_list in resualt_combinations_list:
            if numbers == sum(temp_list):
                resualt_set.add(numbers)
                all_resualt[N] = all_resualt.get(N, 0) + 1
                continue

print(all_resualt)