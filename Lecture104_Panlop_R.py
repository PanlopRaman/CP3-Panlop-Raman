class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart (self):
        print("Added this product to", self.name, self.lastname, "'s cart.")

customer1 = Customer()
customer1.name = "Tom"
customer1.lastname = "Hack"
customer1.addCart()

customer2 = Customer()
customer2.name = "Jerry"
customer2.lastname = "Brow"
customer2.addCart()

customer3 = Customer()
customer3.name = "Pual"
customer3.lastname = "Frix"
customer3.addCart()
