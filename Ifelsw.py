Username = input("Username : ")
Password = input("Password : ")
if Username == "weergaza" and Password == "weer123":
    print("!Done!")
    print("---CalculatorForShop---")
    print("1.VatCalculator")
    print("2.PriceCalculator")
    Userinput = int(input(">>"))
    if Userinput == 1:
        price = int(input("Price : "))
        result = price+(price*7/100)
        print(float(result),"THB")
    elif Userinput == 2:
        price1 = float(input("First Produce  : "))
        price2 = float(input("Second Produce Price : "))
        print(price1 + price2, "THB")
    else:
        print("Input Wrong Number Menu Restart to try again")
else:
    print("Login fail")
