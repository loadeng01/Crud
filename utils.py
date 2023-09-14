def get_password() -> str:
    while True:
        pasword = input("Введите пароль: ")

        if len(pasword) < 8:
            print("Пароль должен содержать минимум 8 символов!")
            continue
        if pasword.islower() == True:
            print("Пароль должен содержать хотя одну заглавную букву")  
            continue
        if pasword.isupper() == True:
            print("Пароль должен содержать хотя одну строчную букву")    
            continue
        break
    return pasword


def get_email() -> str:
    while True:
        emal = input("Введите логин: ")
        if "@" not in emal:
            print("Email должен содержать '@'!")
            continue     
        
        dog = emal.index("@") + 1

        if '.com' == emal[-4:]:
            break
        elif '.ru' == emal[-3:]:
            break
        else:
            print("Почта должна название сервиса которым вы пользуетесь")
            continue

    return emal


def get_name() -> str:
    name = input("Введите свое имя: ").title()
    
    if name.isdigit() == True:
        print("Нельзя вводить цифры")
    else:
        return name
    
    
def get_id() -> int:
    users = get_one()
    if len(users) == 0:
        return 1
    else:
        max_id = max([int(i['id']) for i in users])
        return max_id + 1

    


def post_product():
    with open('data.txt', 'a') as f:
        id = get_id()
        f.write(f'id: {id}\n')

        name = get_name()
        f.write(f'name: {name}\n')

        email = get_email()
        f.write(f'email: {email}\n')

        password = get_password()
        f.write(f'password: {password}\n')

        city = input("Ваш город проживания: ").title()
        f.write(f'city: {city}\n')





def get_one():
    users = get_all()
    num = int(input("Number: ")) - 1
    return users[num]
        

def get_all():
    with open('data.txt') as f:
        use = []
        
        for j in range(get_count() // 5):
            w = {}
            try:
                for i in range(5):
                    users = f.readline().replace("\n", "")
                    dots = users.index(":") + 1
                    a = users[:dots - 1]
                    b = users[dots:]
                    w.setdefault(a, b)
                use.append(w)
            except ValueError:
                print("Список пустой")

    return use

               

def get_count():
    with open('data.txt') as f:
        strok = f.readlines()
        count = 0
        for i in strok:
            if "\n" in i:
                count += 1

    return count 


    



