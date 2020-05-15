menuList = []
priceList =[]
def showBill():
    print("My Order".center(30,"-"))
    for i in range(len(menuList)):
        print(menuList[i],priceList[i], "THB")
        TP = 0
        for price in priceList:
            TP += price
    print("-"*30)
    print("Total price = ",TP, "THB")
    print("Thank You".center(30,"-"))

while True:
    menuName = str(input("Enter menu: "))
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Enter price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
