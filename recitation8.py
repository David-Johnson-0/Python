def genShoppingCart(item, quant, cart):
  cart[item] = quant
  return cart


def getItem():
  item = input("Enter item: ").lower()
  return item


def getQuant():
  quant = int(input("Enter quantity: "))
  return quant


def getCost(quant):
  cost = float(input("Enter cost per item: ")) * quant
  return cost


def printCartbyItem(cart, cost):
  trueItems = sorted(cart.keys())
  for item in trueItems:
    print(f'{cart[item]} {item}: ${cost[item]:.2f}')


def printCartbyCost(cart, cost):
  tempcart = cost
  tempcart = dict(sorted(tempcart.items(), key=lambda x: x[1], reverse=True))
  for item, amount in tempcart.items():
    print(f'{cart[item]} {item}: ${amount:.2f}')


def goShopping():
  cart = {}
  cost = {}
  while True:
    print("\n\nWelcome to Generic E-Commerce Store!")
    print("Which of the following would you like to do?")
    print("1. Add Item\n2. Update Item\n3. Delete Item")
    print("4. View Cart by Name")
    print("5. View Cart by Cost\n6. Quit\n")

    choice = input("Enter choice: ")
    totalCost = 0

    if choice == "1":
      item = getItem()
      quant = getQuant()
      cost[item] = getCost(quant)
      cart = genShoppingCart(item, quant, cart)
      print(f'{quant} {item} added to cart\n')
    elif choice == "2":
      item = getItem()
      if item in cart:
        quant = getQuant()
        cost[item] = getCost(quant)
        cart[item] = quant
        print(f'{quant} {item} updated in cart\n')
    elif choice == "3":
      item = getItem()
      if item in cart:
        del cart[item]
        del cost[item]
        print(f'{item} deleted from cart\n')
    elif choice == "4":
      printCartbyItem(cart, cost)
    elif choice == "5":
      printCartbyCost(cart, cost)
    elif choice == "6":
      for item in cost:
        totalCost += cost[item]
        print(f'{item} ({cart[item]}) at ${cost[item]:.2f} / item')
      print(f'Total amount in cart: ${totalCost:.2f}')
      print("Thank you for shopping with us!")
      break
    else:
      print("Invalid choice\n")