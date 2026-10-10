



def module_op():
    while True:
        print()
        print("="*20)
        print("Explore module")
        print("1. math module")
        print("2. Date and Time Module")
        print("3. UUID's Module")
        print("4. Random Module")
        print("5. Time Module")
        print("6. Back to main menu")
        print()
        print("="*20)


        choice= int(input("Enter Your choice: "))

        if choice == 1:
            import math
            print("Math Module: ")
            print(dir(math))

        elif choice==2:
            from datetime import datetime
            print("Date and Time Module:")
            print(dir(datetime))

        elif choice==3:
            from uuid import uuid4
            print("UUID's Module:")
            print(dir(uuid4))

        elif choice==4:
             import random
             print("Random Module")
             print(dir(random))

        elif choice==5:
            import time
            print("Time Module:")
            print(dir(time))

        elif choice==6:
            print("Going Back to main menu!")
            break

        else:
            print("Invalid choice!!")
            