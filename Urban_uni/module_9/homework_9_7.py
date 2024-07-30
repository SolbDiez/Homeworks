
def is_prime(func):
    def wrapper(*args):
        original_result = func(*args)
        if isinstance(original_result, int):
            print('Простое число')

        else:
            print('Какое то не простое число')
        return original_result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)

result_1 = sum_three(2, 3, 6)
print(result_1)

result_2 = sum_three(2.5, 4, 6)
print(result_2)
