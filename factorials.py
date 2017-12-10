number=int(input("Enter the any number"))
fact=number
sum=0
for i in range(1,number):
    if(number%i==0):
        #print(i)
        sum=sum+i
        #print(sum)
print(sum+number)