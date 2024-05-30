# def summ(n):
#     if n == 1:
#         return 1
#     return n + summ(n - 1)
#
# print(summ(5))


# list_ = [[1, 2, 3, 4], [4, 5], "Hello", {'a': 2, 'b': 3}]

list_ = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]



def flatten(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        return(flatten(s[0]) + flatten(s[1:]))
    return(s[:1] + flatten(s[1:]))
s = [[1, 2], [3, 4], 9]
print("Выпрямленный список: ", flatten(s))

# dic = {'a': 1, 'b': 2, 'c': 8}
# z = 0
# zz = 0
# z = sum(dic.values())
# zz = len(dic.values())
# print(z, zz)




list_ = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    "Hello",
    (6, {'cube': 7, 'drum': 8})
    ]

n = 0
nn = []
for i in list_:
    if isinstance(i, list):
        n += sum(i)
    elif isinstance(i, str):
        n += len(i)
    elif isinstance(i, dict):
        n += sum(i.values())
        n += len(i.keys())



print(n)
print(nn)


# list_ = [1, 2, 3, 4]
# n = 0
# n += sum(list_)
# print(n)






