name=input("Enter your name:")
per=float(input("Enter your percentage:"))
# name=chams
# per=85
if per > 90:
    print(f"Congratulations {name}")
elif per>=80 and per<75:
    print("grade A")
elif per>70 and per<65:
    print("Grade B")
else:
    print("fail")
# ----------------------------------print 1-100 ---------------------------------
# i=1
# while i <= 100:
#     i+=1
#     print(i)

# i=1
# while i <= 100:
#     if i % 2 ==0:
#         print(f"{i}-even")
#     else:
#         print(f"{i}-odd")
#     i+=1