#write a python program to find the absolute value for the difference between in the even and odd
#test case 1:1223
#test case 2:4567
#test case 3:123456789



num=[int(d) for d in str(input("enter number:"))]
even,odd = 0,0
for i in range(0,len(num)):
    if(i % 2 ==0):
        even = even + num[i]
    else:
        odd = odd + num[i]
print(abs(odd-even))        
print(num)       
