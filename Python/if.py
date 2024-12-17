name=input("enter your name:")
age=int(input("Enter your age:"))
if age >= 16 and age < 30:
    weight=float(input("enter your weight:"))
    if weight > 30 and weight < 90:
        print(f"Yes YOU CAN JOIN{name}...")
    else:
        print("sorry ur not eligible bcz ur weight nt matching")   
else:
    print("sorry,your age is not matching!!")