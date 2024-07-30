# def all_variants(text):
#     length = len(text)
#     for x in range(1, length + 1):
#         for y in range(length - x + 1):
#             yield text[y:y + x]
#
# # Пример вызова функции и итерации по результатам
# a = all_variants("abc")
# for i in a:
#     print(i)
"""def all_var(string):
    for length in range(len(string)):
        for index in range(len(string) - length):
            print(string[index:index+length+1])

a = all_var('abc')"""

s = 'abc'

print(range(len(s))) # = 0, 1, 2
print(s[2:4])