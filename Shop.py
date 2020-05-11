username = input("Username : ")
password = input("Password : ")
if username == "weergaza" and password == "weer123":
    print("!done!")
    print("----------------")
    print("    Minimart    ")
    print("----------------")
    print("Menu")
    print("1.Banana : 10THB")
    print("2.Sausage: 20THB")
    print("3.Cola   : 15THB")
    print("Choose your menu")
    Menu = int(input(">> "))
    if Menu == 1:
        Aun1 = input("How many do you want : ")
        print(float(10 * int(Aun1)),"THB")
    elif Menu == 2:
        Aun2 = input("How many do you want : ")
        print(float(20 * int(Aun2)),"THB")
    elif Menu == 3:
        Aun3 = input("How many do you want : ")
        print(float(15 * int(Aun3)),"THB")
    else:
        print("input wrong menu number restart to try again")
else:
    print("login fail")

