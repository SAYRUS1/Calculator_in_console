import lib_if_elif as l


def calc():
    try:
        a = int(input("Введите число: "))
        c = input("Введите знак: ")
        b = int(input("Введите второе число: "))
        if c == "+" or c == "-" or c == "/" or c == "*":
            l.sump(a,b,c)
        else:
            print("Не верный символ")
            calc()     
    except Exception as Fuck0:
        print(Fuck0)
        calc()
calc()



