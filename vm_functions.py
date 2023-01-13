#---------------------------------------- Functions ------------------------------------
#empty items list
items=[]

#loading vending machine products to main n list
def products(): #LETS PUT SOME DEFAULT ITEMS IN THE VENDING MACHINE
    global items
    prod1=VM_prod("A1",2,"Water",5)
    items.append(prod1)
    prod2=VM_prod("A2",5,"Cips",2)
    items.append(prod2)
    prod3=VM_prod("A3",8,"Coke",2)
    items.append(prod3)
    prod4=VM_prod("A4",10,"Gatorade",2)
    items.append(prod4)
    prod5=VM_prod("B1",5,"Iced tea",5)
    items.append(prod5)
    prod6=VM_prod("B2",7,"Cheetos",5)
    items.append(prod6)
    prod7=VM_prod("B3",7,"Doritos",1) 
    items.append(prod7)
    prod8=VM_prod("B4",8,"Pepsi",2)
    items.append(prod8)



#class defining to call items[]
class VM_prod:
    def __init__(self, itemID,price,item_name,stock):
        super().__init__()
        self.itemID = itemID
        self.price = price
        self.item_name = item_name
        self.stock = stock
    def __str__(self):
        print("-"*50)
        print("Item: {} Item Name: {} Price: {} Stock: {}".format(self.itemID, self.item_name,self.price, self.price, self.stock))
        print("-"*50)

# owner adding products function
def add_product():
    global items
    print("   ADD Item")
    itemID = input("Enter Item ID : ")
    price   = float(input("price : $ "))
    iname = input("Item Name: ")
    addingItem = search_dup(itemID) 
    if addingItem != None:
        print("Item alreaady exists. Please input new item")
    else:
        #if this item does not exist. just append to list
        vm = VM_prod(itemID, price, iname)
        items.append(vm)


#buying item
def buy_product():
    print("-"*40)
    print("    Purchase Item")
    print("-"*40)
    global items
    itemID = input("Enter item ID: ")
    buyItem = search_dup(itemID)
    if buyItem != None:
        buyItem.__str__()
        itemPrice = buyItem.price
        if calculate(itemPrice) == True:
            buyItem.stock -= 1
    else:
        print("Invalid Input")

#calculating price, change, and insufficient fund
def calculate(price):
    print("Please pay : $ ", price)
    paid = float(input("Enter your money: $"))
    if paid == price:
        return True
    elif paid > price:
        print(f"Your change is: ${paid-price}")
        print("Succesful")
        return True
    else:
        print(f"You need to add more: ${price-paid}")

#show products menu
def disp_prod():
    global items
    for i in items:
        i.__str__()

#search for product
def search_dup(itemID):
    global items
    for i in items:
        if i.itemID == itemID:
            return i 
    return None

#terminating program
def quit_vm():
    print()
    print("Terminating...")
    exit(0)

#---------------------------------------- Functions ------------------------------------
