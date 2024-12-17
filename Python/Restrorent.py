menu={
    'pizza':40,
    'coffee':120,
    'pasta':80,
    'salad':60,
    'rolls':120
}
print("Well come to Shreya Restro")
print("Pizza:40\n Pasta:80\n Coffee:120\n Salad:60\n Rolls:120")

order_total=0

item_1=input("Enter the name of item u want Order:")

if item_1 in menu:
    order_total=order_total+menu[item_1]
    print(f" your item {item_1}has to be added to ur Order:")

else:
    print(f" Ordered item{item_1} is not available yet!!")

while(True):
    another_order=input("Do u want Order another item Yes/No!")

    if(another_item=="Yes"):
        item_2=input("Enter the name of next item!")

        if item_2 in menu:
            order_total=order_total+menu[item_2]
            print(f"Item{item_2} has been added to ur Order!!")

        else:
            print(f" Ordered item{item_2} is not available yet!!")
    
    elif(another_order=="No")
        print("Thank you for Ordering!!")
        break
             