#write a program to add 6 user defined numbers and return the value to the
#test case value:8 6 4 2 10 0

def num(a,b,c,d,e,f):
    return(a+b+c+d+e+f)
a=int(input("enter the value "))
b=int(input("enter the value "))
c=int(input("enter the value "))
d=int(input("enter the value "))
e=int(input("enter the value "))
f=int(input("enter the value "))
result=num(a,b,c,d,e,f)
print("output of the evalution is ",result)