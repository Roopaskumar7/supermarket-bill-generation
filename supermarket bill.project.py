from datetime import datetime

name = input("enter your name:")
# List of items
lists= '''
Rice       Rs 20/kg
salt       Rs 20/kg
Maggie     Rs 50/kg
oil        Rs 180/liter
sugar      Rs 20/kg
biscuits   Rs 20/pack
chocolate  Rs 20/pack
Drinks     Rs 50/bottle
colgate    Rs 20/each
panner     Rs 110/kg
'''

#declartion
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates
items={  'rice': 20,
         'salt': 20,
         'Maggie': 50,
         'oil':180,
         'sugar': 20, 
         'biscuits': 20, 
         'chocolate': 20, 
         'Drinks': 50,
         'colgate': 20,
         'Panner': 110}
option= int(input("for list of items press 1:"))
if option== 1:
    print(lists)

for i in range(len(items)):
    inp1= int(input("if you want to buy press 1 or 2 for exist:"))
    if inp1==2:
        break

    if inp1== 1:
        item = input("Enter your items:")
        quantity = int(input("Enter your quantity:"))

        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,item,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry the item you entred is not available")
    else:
         print("sorry you entred the wrong number")

    inp=input("can i bill your items yes or no:")

    if inp=='yes':
           pass
           if finalamount != 0:
            print(25*"=","RK SuperMarket",25*"=")
            print(28*" ", "Kakinada")
            print("Name:",name,30*" ", "Date:",datetime.now())
            print(75*"-")
            print("sno",8*"",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*'', 1*' ', ilist[i],8*' ',qlist[i], 10*" ",plist[i])
                print(75*"-")
                print(50*"-",'TotalAmount:' 'Rs',totalprice)
                print("gst amount",40*" ",'Rs', gst)
                print(75*"-")
                print(50*"-",'finalAmount:' 'Rs',finalamount)
                print(75*"-")
                print(20*"-","Thanks For Visting")
                print(75*"-")

                

























