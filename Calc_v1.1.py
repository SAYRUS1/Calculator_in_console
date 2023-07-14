import lib_if_elif as l


def data_entry():
    try:
        a = int(input("Введите число: ")) 
        b = int(input("Введите второе число: "))
        c = input("Введите знак: ")
        if c == "+" or c == "-" or c == "/" or c == "*":
             l.sump(a,b,c)
        else:
            print("Введите знак!")
            data_entry()   
    except Exception as Fuck0:
        print(Fuck0)
        data_entry()
    except KeyboardInterrupt:
        print("\nSIGINT:Exit is Program Ctrl+C")
data_entry()

