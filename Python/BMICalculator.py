
weight=float(input("Enter your weight in kg:"))
if(weight>250):
   print("Invalid")
else:
    height=float(input("Enter your height in meters:"))
    if(height>300):
        print("Invalid")
    else:  
        bmi=weight/(height*height);
        print(bmi)

        if(bmi< 18.5):
            print("underweight")
    

        elif(18.5 <= bmi < 25):
            print("normal")

        elif(bmi <=30  and 34.5):
            print("overweight")
           
        else:
            print("Obese")

            


