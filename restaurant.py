print("welcome to miro restaurant")
from menu import menu

for categorie in menu.keys():
        print(categorie)
        for ID , article_info in menu[categorie].items():
            for article, price in article_info.items():
                print( "   "+ ID +" . "+ article +" "+ str(price) +" $")


order = []
while categorie in menu.keys():
    take_order = input("what would you like to order ")
    if take_order in menu[categorie].keys():
        order.append(take_order)
    elif take_order == "0":
        break
    else:
        print("sorry we don't offer that") 

prices_ordered = []
print("receipt")

for order_ID in order:
    for categorie in menu.keys():
        if order_ID in menu[categorie].keys() :
            for ID , article_info in menu[categorie].items():
                for article, price in article_info.items():
                    print(ID +" . "+ article +" "+ str(price) +" $")
                    prices_ordered.append(price)

total_price = sum(prices_ordered)
print("the total amount is: "+str(total_price))
print("thank you very much for your visit")
