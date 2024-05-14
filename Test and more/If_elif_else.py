# age = input('Your age?')
# try:
#     i = int(age)
# except ValueError:
#     i = None
#
# if isinstance(i, int) and int(age) >= 18:
#     print('YES')
# elif isinstance(i, int) and int(age) < 18:
#     print('NO')
# else:
#     print('Enter only integers plz')

age = input('Enter your age ')
if age.isdigit() and int(age) >= 18 and int(age) < 100:
    print('come in')
elif age.isdigit() and int(age) < 18:
    print("get out!")
elif age.isdigit() and int(age) > 100:
    print("you're dead unfortunately")
else:
    print('enter only numbers please')