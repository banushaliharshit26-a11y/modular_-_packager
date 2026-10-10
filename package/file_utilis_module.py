def files():
    while True:
        print()
        print("=="*20)
        print("File Operations :")
        print("=="*20)
        print("1. Create a New File ")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File ")
        print("5. Update to a File ")
        print("6. Back to Main Menu")
        print("=="*20)

        ch=int(input("Enter Your Choice : "))

        if ch==1:
            file_op()
          
        elif ch==2:
            add_entry()
        elif ch==3:
            read_entry()
        elif ch==4:
             append_op()

        elif ch==5:
            update_entry()

        elif ch==6:
            print("Going Back to Main Menu....")
            break
        else:
            print("Invalid Choice (1-6)!")

def file_op():
    try:
        name=input("Enter a file Name (example.txt): ")
        with open(name,"x") as file:
            print("file succesfully created")
            pass
    except:
        ("Enter a valid file name!!")
def add_entry():
    try:
        name=input("Enter a file name: ")
        entry=input("Enter a entry: ")
        with open(name,"a") as file:
             file.write(entry+"\n")
        print("Message added succefully")
    except:
        print("Enter a valid message")

def read_entry():
    try:
            name=input("Enter a file Name: ")
            with open(name,"r") as file:
                print("File Content :")
                print (file.read())
    except:
         print("Enter a valid File Name!!")

def append_op():
    try:
            name=input("Enter a File Name: ")
            with open (name,"a") as file:
                entry= input("Enter a Entry: ")
                file.write(entry)
    except:
         print("Something went Wrong!!")
           
def update_entry():
        try:
                name=input("Enter a File Name: ")
                with open(name,"r") as file:
                    see= file.readlines()
                    search=input("Enter a keyword for see entry: ")
                    for x in see: 
                        if search.lower() in x.lower() :
                              print(x)
                              break
                    else:
                         print(f"no entries found for the keyword: {search}")
        except:
             print("Something Went Wrong")
            