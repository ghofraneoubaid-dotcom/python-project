from menu import menu

print("welcome to miro restaurant")

def get_menu(menu):
    for categorie in menu.keys():
        print(categorie)
        for ID , article_info in menu[categorie].items():
            for article, price in article_info.items():
                print("   "+ ID +" . "+ article +" "+ str(price) +" $")

order = []          # liste globale des commandes

def take_orders(menu):
    while True:
        take_order = input("what would you like to order (enter 0 to stop) ")
        if take_order == "0":
            break
        for categorie in menu.keys():
            if take_order in menu[categorie].keys():
                order.append(take_order)
                break
            else:
                print("sorry we don't offer that")

prices_ordered = [] # liste globale des prix

def receipt(menu):
    print("receipt")
    for order_ID in order:
        for categorie in menu.keys():
            if order_ID in menu[categorie].keys():
                article_info = menu[categorie][order_ID]
                for article, price in article_info.items():
                    print(order_ID +" . "+ article +" "+ str(price) +" $")
                    prices_ordered.append(price)
    return prices_ordered
        
def calcul_price(prices_ordered):
    total_price = sum(prices_ordered)
    print("the total amount is: "+str(total_price))

print("thank you very much for your visit")

def restaurant():
    from menu import menu
    get_menu(menu)                        # affiche le menu
    take_orders(menu)                     # prend les commandes
    prices_ordered = receipt(menu)        # génère le reçu
    calcul_price(prices_ordered)          # calcule le total
    
restaurant()
