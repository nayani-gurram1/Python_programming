def eComm():
    cart=[]
    while True:
        print("\nCart Operations")
        print("1.Add Product")
        print("2.Remove Product")
        print("3.Search Product")
        print("4.Display Cart")
        print("5.Count Product")
        print("6.Sort the cart items")
        print("7.Clear the cart")
        print("8.Exit")
        choice=int(input("\nEnter the choice:"))
        if choice==1:
            product=input("Enter the product to add:")
            cart.append(product)
            print(f"Product '{product}' is added")
        elif choice==2:
            product=input("Enter the product:")
            if product in cart:
                cart.remove(product)
                print(f"Product '{product}' is removed")
            else:
                print(f"Product '{product}'is not exist in cart")
        elif choice==3:
            product=input("Enter the product:")
            if product in cart:
                print(f"Product '{product}' is in cart")
            else:
                print(f"Product '{product}' is not in cart")
        elif choice==4:
            print("Cart:", cart if cart else "Cart is empty.")
        elif choice == 5:
            print(f"Total products in cart: {len(cart)}")

        elif choice == 6:
            print(f"Sorting the cart: {cart.sort()}")
        elif choice==7:
            print(f"Clear the cart: {cart.clear()}")
        elif choice==8:
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")
eComm()



