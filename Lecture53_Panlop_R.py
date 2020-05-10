price = float(input("Enter product price: "))
def vatCal(TP):
    result = TP+(TP*7/100)
    return result
print("Total Price includea VAT : ", (vatCal(price)), "THB")
