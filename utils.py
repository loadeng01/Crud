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
                    b = users[dots + 1:]
                    w.setdefault(a, b)
                use.append(w)
            except ValueError:
                print("Список пустой")

    if len(use) < 1:
        return "База данных пуста"
    else:
        return use
    

def get_one():
    try:
        users = get_all()
        num = int(input("Id аккаунта: ")) - 1
        print(users[num])
    except IndexError:
        print("Аккаунта с таким ID нету")

        


def get_count():
    with open('data.txt') as f:
        strok = f.readlines()
        count = 0
        for i in strok:
            if "\n" in i:
                count += 1

    return count 


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
    users = get_all()
    
    if type(users) == str:
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

    print("Аккаунт сохранен")


def re_write(users):
    delete_all()

    ids = [*range(1,len(users) + 1)]
    with open('data.txt', 'w') as f:
        for i in range(len(users)):
            
            f.write(f'id: {ids[i]}\n')

            name = users[i]['name']
            f.write(f'name: {name}\n')

            email = users[i]['email']
            f.write(f'email: {email}\n')

            password = users[i]['password']
            f.write(f'password: {password}\n')

            city = users[i]['city']
            f.write(f'city: {city}\n')



def patch():
    try:
        users = get_all()
        num = int(input("Id аккаунта: "))
        num = num - 1

        users[num]['name'] = get_name()
        users[num]['email'] = get_email()
        users[num]['password'] = get_password()
        users[num]['city'] = input("Ваш город проживания: ").title()

        re_write(users)
        print("Аккаунт изменен")

    except IndexError:
        print("Аккаунта с таким ID нету")

    

           
def delete_all():
    with open('data.txt', 'w') as f:
        f.write("")
    print("Вся база данных удалена")

def del_one():
    try:
        users = get_all()
        num = int(input("Id аккаунта: "))
        num = num - 1
        users.pop(num)
        re_write(users)
        print("Аккаунт удален")
    except IndexError:
        print("Аккаунта с таким ID нету")



def main():
    print("""Представляем вашему вниманию Систему CRUD
          Bам доступны следущие фукции:
          Создать новый аккаунт: 1
          Изменить аккаунт: 2
          Показать все аккаунты: 3
          Показать аккаунт: 4
          Удалить аккаунт: 5
          Удалить все аккаунты: 6""")
    
    try:
        choice = int(input("Что выберите: "))

        if choice == 1:
            post_product()
        elif choice == 2:
            patch()
        elif choice == 3:
            get_all()
        elif choice == 4:
            get_one()
        elif choice == 5:
            del_one()
        elif choice == 6:
            delete_all()
        else:
            print("Других функций у нас к сожалению нету")
    except ValueError:
        print("Вводите только цифры!")







