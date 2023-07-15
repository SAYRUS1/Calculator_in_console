import lib_if_elif as l


def data_entry():
    try:
        a = int(input("1 Enter the operand: ")) 
        b = int(input("2 Enter the operand: "))
        c = input("Enter the operand: ")
        if c == "+" or c == "-" or c == "/" or c == "*":
             l.sump(a,b,c)
        else:
            print("Select the action + - * /   ?:")
            data_entry()   
    except Exception as Fuck0:
        print(Fuck0)
        data_entry()
    except KeyboardInterrupt:
        print("\nSIGINT:Exit is Program Ctrl+C")
data_entry()

