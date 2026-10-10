from package import dt_operations
from package import math_op
from package import random_op,uuid_op,files,module_op



def main():
    while True:
        print("===================")
        print("Welcome to multi_utililty Toolkit")
        print("===================")
        print("Choose a Option!")
        print("1. Datetime and Time Operations:")
        print("2. Mathematical Operations:")
        print("3. Random Data Generation:")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations: ")
        print("6. Explore Module Attributes: ")
        print("7. Exit")
        print("=======================")


        choice=int(input("Enter Your Choice (1-7): "))

        if choice==1:
            dt_operations()
        elif choice == 2:
            math_op()

        elif choice==3:
            random_op()

        elif choice==4:
            uuid_op()

        elif choice==5:
            files()

        elif choice==6:
            module_op()

        elif choice==7:
            print("Thank you for using Multi-Utility Toolkit!")
            break



if __name__=="__main__":
    main()

