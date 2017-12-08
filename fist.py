#Add your code here
def converToDollar(amount):
    ruppees=amount*65
    totalamount=ruppees-(ruppees*1)/100
    return totalamount
amount=int(input("Enter the number of dollars:"))
total=converToDollar(amount)
print(total)