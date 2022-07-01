import string
while True:
    x = int(input("Введите первое число : "))
    y = int(input("Введите второе число : "))
    print("Если хотите сложить числа нажмите + ")
    print("Если хотите отнять числ нажмите - ")
    print("Если хотите умножить числа нажмите * ")
    print("Если хотите поделить числа нажмите / ")
    s = input("Выберите действие: ")
    if s == '+':
        res = x + y
        print("Результат сложения равен : ", res)
    elif s == '-':
        res2 = x - y
        print("Результат вычитания равен : ", res2)
    elif s == '*':
        res3 = x * y
        print("Результат умножения равен : ", res3)
    elif s == '/':
        if y != 0:
            res4 = x / y
            print("Результат деления равен : ", res4)
        else:
            print("На ноль делить нельзя!!!")
    my_string_1 = input("Желаете продолжить: 'YES' 'NO' ")
    my_string_1 = my_string_1.lower()
    go_str = 'yes'
    ex_str = 'no'
    if my_string_1 == go_str:
        print("Продолжим!")
        continue
    elif my_string_1 == ex_str:
        print("Выход")
        break


