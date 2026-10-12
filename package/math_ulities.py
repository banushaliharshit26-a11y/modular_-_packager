from datetime import datetime
import time
import math
from uuid import uuid4
import random
import string
def dt_operations():
    while True:
        print()
        print("Datetime and Time Operations:")
        print("-"*20)

        print("1.Display current Date and Time")
        print("2. Calculate Difference Between two dates/times")
        print("3. Format date into custom format:")
        print("4. stopwatch:")
        print("5. countdown timer:")
        print("6. Back to menu:")
        print("-"*20)


        choice=int(input("Enter your Choice: "))
        if choice== 1 :
            dt=datetime.now()
            print(f"Current Date and Time: {dt} ")

        elif choice== 2 :
            frist=input("Enter the First date (YYYY-MM-DD): ")
            second=input("Enter the second date (YYYY-MM-DD): ")

            dt1=datetime.strptime(frist,"%Y-%m-%d")
            dt2=datetime.strptime(second,"%Y-%m-%d")
            print(f"Difference:{abs(dt1-dt2)}")

        elif choice == 3 :
            current_dt=datetime.now()
            print("select a option")
            print("1. Date")
            print("2. Time")
            print("3.Datetime")

            choice=int(input("Enter a Choice: "))
            if choice == 1:
                print(f"current date {datetime.now().strftime("%Y-%m-%d")}")

            elif choice == 2:
                print(f"current time {datetime.now().strftime("%H-%M-%S")}")

            elif choice == 3:
                print(f"current Date-time {datetime.now()}")

            else:
                print("invalid choice!")

        elif choice == 4:
            start= time.time()
            users=input("Enter for Stopwatch")
            end=time.time()
            print(f"Total time is : {end-start}")

        elif choice == 5:
            timer=int(input("Enter a Timer: "))
            while timer > 0 :
                print(timer)
                time.sleep(1)
                timer= timer-1

        elif choice==6:
            break

def math_op():
    while True:

            print()
            print( "Mathematical Operations !")
            print("-"*20)
            print("1. Calculate Factorial")
            print("2. Solve Compound Interest")
            print("3. Trigometric Calculations")
            print("4. Area of Geometric Shapes")
            print("5. Back to menu")
            print("-"*20)

            choice=int(input("Enter your Choice: "))
            if choice==1:
                fact=int(input("Enter a number for factorial: "))
                print(f" Factorial Number : {math.factorial(fact)}")

            elif choice==2:
                money=int(input("Enter amount: "))
                rate=int(input("enter rate of interest (in %): "))
                year=int(input("Enter time(in years): "))

                calculation=money*(1+rate/100)**year
                print(f"Difference : {calculation}")

            elif choice == 3:
                value=float(input("Enter a degree: "))
                value= math.radians(value)
                print(f"sin :{math.sin(value)}")
                print(f"cos : {math.cos(value)}")

            elif choice==4:
                print("1. Area of circle")
                print("2. Area of rectangle")

                choice=int(input("Enter your choice: "))
                if choice==1:
                    r=float(input("Enter a radius: "))
                    area= math.pi*r*r
                    print(f"Area of circle: {area}")
                elif choice==2:
                        i=float(input("enter a value: "))
                        b=float(input("enter a value: "))
                        c=i*b
                        print(f"Area of rectangle: {c}")
            

            elif choice==5:
                print("Going back to main menu!")
                break

            else:
                print("Invalid choice!!")

def uuid_op():
    while True:
        print()
        print("Unique Identifiers!")
        print("---------------")
        print("1. Create a uuid")
        print("2. back to menu")
        print("----------------")

        choice=int(input("Enter a chocie: ")) 

        if choice==1:
            id=uuid4()
            print(f" Generated uuid is : {id}")

        elif choice==2:
            print("Going back to main menu!")
            break
        else:
            print("Invalid choice!!")

def random_op():
    while True:
        print()
        print("Random Data Generations")
        print("-"*20)
        print("1. Random Number")
        print("2. Random list")
        print("3. create password")
        print("4. for otp")
        print("5. back to menu")
        print("-"*20)
        choice=int(input("Enter a chocie: "))

        if choice==1:
            num= random.randint(1,99)
            print(f"random number is : {num}")

        elif choice==2:
            l=[1,55,78,98,65,42,12,35,62,0]
            random.shuffle(l)
            print(f"random list is: {l}")

        elif choice==3:
            len=int(input("Enter length of password: "))
            c=string.ascii_letters+string.punctuation+string.digits
            password="".join(random.choices(c,k=len))
            print(f" create password: {password}")

        elif choice==4:
            op=random.randrange(100000,999999)
            print(f"OTP is: {op}")

        elif choice==5:
            print("Going back to main menu!")
            break
        else:
            print("invalid choice!!")

