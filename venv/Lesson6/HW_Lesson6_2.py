import keyword
# Переменная не может начинаться с цифры, состоять только из цифр, не может содержать заглавные буквы и знаки пунктуации,
# кроме нижнего подчеркивания "_" . Также, она не может быть ни одним из зарегистрированных слов.
# При этом имя переменной, может состоять только из одного нижнего подчеркивания "_" .
# Зарегистрированные слова можно взять из keyword.kwlist.
#
# В итоге проверки, на печать выводится True, если такое имя переменной допустимо, и False - в противном случае.
while True:
    s = input("Введите название переменной: ")
    checking_keyword = keyword.kwlist
    #print(checking_keyword)
    checking_dot = ','
    checking_point = '.'
    checking_underscore = '_'
    checking_user_upper = s.upper()
    checking_low_string = s.islower()
    user_string = s
    if s[0].isdigit():
        print("Переменная не может начинаться с числа!")
    elif user_string in checking_keyword:
        print("Вы не можете использовать уже зарезервированные имена переменных!")
    elif user_string.count(checking_dot) == checking_dot:
        print("Имя переменной не может включать запятую!")
    elif user_string.count(checking_point) == checking_point:
        print("Имя переменной не может содержать точку!")
    elif user_string == checking_underscore:
        print("Имя переменной подходит!!!")
        break
    elif user_string.islower():
        print("Good")
        break
    # elif user_string.count(user_string) == user_string.isupper():
    #     print("Переменная не может содержать большую букву")
    else:
        print("Переменная не может содержать большую букву")


