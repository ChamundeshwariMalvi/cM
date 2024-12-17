# def sum(a,b):
#     s=a+b
#     return s
# print(sum(5,7))   --------------------------------------functions----------------------------



# def bill(amt,unit):
#     total_printing=unit+" "+amt
#     return total_printing

# print(bill("50",  "Rs"))

# ---------------------------------------Python program to convert the currency----------------------------
# -------------------------------------------------------------of one country to that of another country 


def converter(amt,unit="USD"):
    if(unit=="Rs"):
        total=int(amt)/83
        return total
        
    elif(unit=="eur"):
        total=float(amt)*1.05
        return total

    elif(unit=="dhr"):
        total=float(amt)*2.65
        return total
    
    else:
        return amt+unit

print(converter("150","dhr"))