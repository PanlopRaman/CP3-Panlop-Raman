price = float(input("Enter product price: "))
def vatCal(TP):
    result = TP+(TP*7/100)
    return result
print("Total Price included VAT : ", (vatCal(price)), "THB")
