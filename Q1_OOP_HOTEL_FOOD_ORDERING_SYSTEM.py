#Develop a python application to maintain hotel food order records 
#create the following classes: Order:"customer name" "food item","order amount",categorize orders as: "veg" "non veg"
#implement methods to display order details. 
#Restaurant: "Add order records" "display all orders"



class Order:
    def __init__(self, customer_name, food_item, order_amount, category):
        self.customer_name = customer_name
        self.food_item = food_item
        self.order_amount = order_amount
        self.category = category

    def display_order(self):
        print("\nCustomer Name :", self.customer_name)
        print("Food Item      :", self.food_item)
        print("Order Amount   : Rs.", self.order_amount)
        print("Category       :", self.category)


class Restaurant:
    def __init__(self):
        self.orders = []

    def add_order(self):
        customer_name = input("Enter Customer Name: ")
        food_item = input("Enter Food Item: ")
        order_amount = float(input("Enter Order Amount: "))

        print("Select Food Category:")
        print("1. Veg")
        print("2. Non Veg")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            category = "Veg"
        elif choice == 2:
            category = "Non Veg"
        else:
            print("Invalid Category!")
            return

        order = Order(customer_name, food_item, order_amount, category)

        self.orders.append(order)

        print("\nOrder Added Successfully!")


    def display_all_orders(self):
        if len(self.orders) == 0:
            print("\nNo Order Records Found!")
        else:
            print("\n===== ALL FOOD ORDER DETAILS =====")

            for order in self.orders:
                order.display_order()



restaurant = Restaurant()

while True:
    print("\n===== HOTEL FOOD ORDER MANAGEMENT =====")
    print("1. Add Order")
    print("2. Display All Orders")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        restaurant.add_order()

    elif choice == 2:
        restaurant.display_all_orders()

    elif choice == 3:
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")


    
