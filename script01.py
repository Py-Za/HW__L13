list_a = [3, 6, "a", 8, 2, "c", "2c"]
# Przekształć ją do postaci ["3", "6", "8", "2"] (tak, to mają być stringi) przy pomocy list comprehension
list_aa = [str(x) for x in list_a if type(x) == int]

list_b = ["aabcd", "ha", "z", "gabcdef", "dab"]
# Przy pomocy argumentu key funkcji sort posortuj ją wg. długości ciągów znaków, od najkrótszego, do najdłuższego
list_bb = sorted(list_b, key=len)

list_c = [2, 5, 6, 8, 1, 3, 12]
# Przekształć ją do postaci [102, 106, 108, 112] przy pomocy list comprehension
list_cc = [100 + x for x in list_c if x % 2 == 0]

list_d = [2, 5, 6, 8, 1, 3, 12]
# Przy pomocy funkcji filter przekształć tę listę tak, by zostały w niej tylko te elementy, które podniesione do potęgi są mniejsze niż 20.
list_dd = list(filter(lambda x: x * x > 20, list_d))

print(f"{list_aa}\n{list_bb}\n{list_cc}\n{list_dd}")
