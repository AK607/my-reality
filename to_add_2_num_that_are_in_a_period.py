a=int(input("enter the 1st number: "))
b=int(input("enter the 2nd number: "))
if a>=-1000 and a<=1000 and b>=-1000 and b<=1000:
    sum=a+b
    print("%d + %d = %d"%(a,b,sum))
else:
    print("the one/more input number(s) are outside the limits")    