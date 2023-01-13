#Python Vending Machine

import vm_functions

#Customer should be able to see products, buy, get change.
#Should have owner dashboard where owner can add items.

print("\nWelcome traveler to...")
print("\t                  █▀▄ ▄▀█ █▄▄ █░░ █▀█ █▀█ █▄░█   █▀█ █▄█ ▀█▀ █░█ █▀█ █▄░█")
print("\t                  █▄▀ █▀█ █▄█ █▄▄ █▄█ █▄█ █░▀█   █▀▀ ░█░ ░█░ █▀█ █▄█ █░▀█")
print()
print("██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗")   
print("██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝")   
print("╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░")   
print("░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░")     
print("░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗")   
print("░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝")   
print("-"*112)

#owner log in
def user():
    while True:
        print("\nIf you are customer enter space")
        password = input("Enter owner password")
        if password == "1234":
            return password
        elif password == " ":
            return password
        else:
            print("Invalid ID")

# customer dashboard
def cust_dash():
    while True: 
        print("\nHere, you use your dabloons that you have collected throughout your journey!")
        print("-"*40)
        print("█▀▄ ▄▀█ █▄▄ █░░ █▀█ █▀█ █▄░█   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀")
        print("█▄▀ █▀█ █▄█ █▄▄ █▄█ █▄█ █░▀█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄")
        print("-"*40)
        print("\n\tHere are the available products")
        vm_functions.disp_prod()
        print("")
        print("C1. Buy")
        print("C2. Quit")
        choice = input("Choose your option: ")
        if choice == "C1":
            vm_functions.buy_product()
        elif choice == "C2":
            vm_functions.quit_vm()

#owner dashboard
def owner_dash():
    while True:
        print("-"*40)
        print("█▀█ █░█░█ █▄░█ █▀▀ █▀█   █▀▄ ▄▀█ █▀ █░█ █▄▄ █▀█ ▄▀█ █▀█ █▀▄")
        print("█▄█ ▀▄▀▄▀ █░▀█ ██▄ █▀▄   █▄▀ █▀█ ▄█ █▀█ █▄█ █▄█ █▀█ █▀▄ █▄▀")
        print("\nRemaining Stock:")
        vm_functions.disp_prod()
        print("-"*40)
        print("01. Buy")
        print("02. Add")
        print("03. Quit")
        choice = input("Choose your option: ")
        if '1' in choice:
            vm_functions.buy_product()
        elif '2' in choice:
            vm_functions.add_product()
        elif '3' in choice:
            vm_functions.quit_vm()

#main program
def main():
    vm_functions.products()
    log_in = user()
    while True:
        print("\n")
        print("Welcome to python vending machine")
        print()
        if log_in == "1234":
            option=owner_dash()
        elif log_in == " ":
            option=cust_dash()
            break


if __name__ == '__main__':
    main()