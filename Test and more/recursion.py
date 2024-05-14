def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)  # суммирует в скобках n -1 до 0 ((5-1) + (4-1) + (3-1) и т.д.

print(summa(5))

# factorial
def fac(n):
    if n == 1:
        return 1
    else:
        return fac(n - 1) * n

print(fac(5))