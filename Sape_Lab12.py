def displaymenu():
    print("---WELCOME TO JERHSE'S TAPSIHAN---")
    print("[1] HOTSILOG - 50 pesos")
    print("[2] SISIGSILOG -60 pesos")
    print("[3] LONGSILOG - 70 pesos")
    print("[4] TAPSILOG - 80 pesos")
    print("[5] PORKSILOG - 90 pesos")
    print("[6] Done")
    
def ordersel():
    selected = []
    while True:
        choice = int(input("Enter your order (please choose from the menu [1-5]: "))
        if choice == 6:
            break
        selected.append(choice)
    return selected

def calcutotal(selectedlist):
    if not selectedlist:
        return selectedlist
    else:
        total = 0
        for x in selectedlist:
            if x == 1:
                total += 50
            if x == 2:
                total += 60
            if x == 3:
                total += 70
            if x == 4:
                total += 80
            if x == 5:
                total += 90
        return total

def cashprocess(total, selectedlist):
    if not selectedlist:
        print("No orders")
    else:
        myitems = {
            1 : "HOTSILOG",
            2 : "SISIGSILOG",
            3 : "LONGSILOG",
            4 : "TAPSILOG",
            5 : "PORKSILOG"
        }
        cash = int(input("Enter your cash: "))
        while True:
            if cash > total:
                cash -= total
                print("\n---Receipt----")
                for x in selectedlist:
                    for z, y in myitems.items():
                        if x == z:
                            print(f"{z} : {y}")
                print(f"\nTOTAL: {total} Change: {cash}")
                break
            else:
                print("Insufficient cash, please enter a valid amount.")
                cash = int(input("Enter your cash: "))

           
def mainprocess():
        displaymenu()
        order = ordersel()
        amount = calcutotal(order)
        cashprocess(amount, order)
        
mainprocess()