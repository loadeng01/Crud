from utils import main

while True:
    main()
    choice = input("Хотите продолжить? Y/N: ").upper()

    if choice == 'Y':
        continue
    elif choice == 'N':
        break