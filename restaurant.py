price =0
while True:
    print("1 IDLI(30) 2 VADA (20) 3 DOSA (55) 4 EXIT")
    ch = input("Enter choice ")
    match ch:
        case "1":
          qty=int(input("Enter the qty = "))
          price += qty*30
        case "2":
          qty=int(input("Enter the qty = "))
          price += qty*20
        case "3":
          qty=int(input("Enter the qty = "))
          price += qty*55
        case "4":
          print("BILL =========",price)
          break
        case _:
          print("Invalid choice ")
