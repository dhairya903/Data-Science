class Seller:
    def __init__(self):
        self.products_quantity = {}
        self.products_price = {}
        self.sales = 0

    def update(self):
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = int(input("Enter selling price: "))
        self.products_quantity[name] = quantity
        self.products_price[name] = price

    def show(self):
        if self.products_quantity == {}:
            print("NO PRODUCTS !!!")
        else:
            print('\nPRODUCTS\n')
            for i, j in self.products_quantity.items():
                print(i.ljust(15), j)

    def buy(self, name, quantity):
        if quantity > self.products_quantity.get(name):
            print("Sorry we don't have enough quantity")
        else:
            self.products_quantity[name] -= quantity
            self.sales += self.products_price[name] * quantity


class Buyer:
    def __init__(self):
        self.cart = {}
        self.quantity = {}
        self.total_amount = 0

    def search(self, seller, name):
        if seller.products_quantity.get(name):
            print("Quantity: " + str(seller.products_quantity.get(name)))
            print("Price per product: " + str(seller.products_price.get(name)))
            add = input("Do want to add this in cart? y/n: ")
            if add == 'y' or add == 'Y':
                quantity = int(input("Enter quantity: "))
                if quantity > seller.products_quantity.get(name):
                    print("Sorry we don't have enough quantity")
                    self.search(seller, name)
                else:
                    self.cart[name] = seller.products_price.get(name) * quantity
                    self.quantity[name] = quantity
                    self.total_amount += seller.products_price.get(name) * quantity
            else:
                pass
        else:
            print("Your requested product does not exist")

    def show(self):
        print('\nYOUR CART')
        for i, j in self.cart.items():
            print(i.ljust(20), j)

    def buy(self, seller):
        self.show()
        print("Total amount: ".ljust(20) + str(self.total_amount))
        confirm = input("Confirm y/n: ")
        if confirm == 'y' or confirm == 'Y':
            for name, quantity in self.quantity.items():
                seller.buy(name, quantity)
        else:
            pass


loop = True
seller = Seller()
buyer = Buyer()
while loop:
    choice = input("Select:\n\t1) Buyer\n\t2) Seller\n")
    if choice == '1':
        option = True
        while option:
            print("\nSelect:\n\t1) Search item\n\t2) Buy items\n\t3) Exit\n")
            choice = input()
            if choice == '1':
                name = input("Enter name of product: ")
                buyer.search(seller, name)
            elif choice == '2':
                buyer.buy(seller)
            elif choice == '3':
                option = False
            else:
                print("Please enter valid choice")
                print("\nSelect:\n\t1) Search item\n\t2) Buy items\n\t3) Exit\n")
    elif choice == '2':
        option = True
        while option:
            print("\nSelect:\n\t1) Update items\n\t2) Show items\n\t3) Exit\n")
            choice = input()
            if choice == '1':
                seller.update()
            elif choice == '2':
                seller.show()
            elif choice == '3':
                option = False
            else:
                print("Please enter valid choice")
                print("\nSelect:\n\t1) Update items\n\t2) Show items\n\t3) Exit\n")
    else:
        print("Please enter valid choice")
        choice = input("Select:\n\t1)Buyer\n\t2)Seller\n")
