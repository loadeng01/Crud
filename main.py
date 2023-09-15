from utils import main
print("Представляем вашему вниманию Систему CRUD")
while True:
    main()
    choice = input("Хотите продолжить? Y/N: ").upper()

    if choice == 'Y':
        continue
    elif choice == 'N':
        break