password_false = True
while password_false:
    length = 0
    upper = 0
    lower = 0
    password = input('Придумайте пароль: ')
    if len(password) > 8:
        length = 1
    for i in password:
        if i.isupper():
            upper = 1
    for i in password:
        if i.islower():
            lower = 1
    print(length, upper, lower)
    if (not length) | (not upper) | (not lower):
        print('Допустимым считается пароль, который состоит более чем из 8 символов'
              ' и включает как прописные, так и заглавные буквы')
    else:
        print(f'Ваш пароль: {password}')
        password_false = False
