print("welcome to miro restaurant")
pizza={100:{"pizza pargherita":5 },
       101:{"pizza tuna":6},
       102:{"pizza mushroom":7}}
print("pizzas")
for i in pizza.keys():
        for j, m in pizza[i].items():
            print(str(i)+" . "+j+" "+str(m)+" $")
casseroles={200:{"pasta casserole":8 },
           201:{"potato casserole":9}}
print("casserole")
for y in casseroles.keys():
    for n, z in casseroles[y].items():
        print(str(y)+" . "+n+" "+str(z)+" $")
list=[]
k=int(input("what would you like to order "))
list.append(k)
while True:
    k=int(input(""))
    if k in casseroles.keys() or k in  pizza.keys():
        list.append(k)
    elif k==0:
         break
    else:
        print("sorry we don't offer that") 
l1=[]
print("receipt")
for l in list:
    if l in pizza.keys() :
        for j, m in pizza[l].items():
            print(str(l)+" . "+j+" "+str(m)+" $")
            l1.append(m)
    elif l in casseroles.keys():
        for j, m in casseroles[l].items():
            print(str(l)+" . "+j+" "+str(m)+" $")
            l1.append(m)
total=sum(l1)
print("the total amount is: "+str(total))
print("thank you very much for your visit")
