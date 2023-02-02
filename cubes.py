#write a python program to make a list of cubes till the value n
#test case 1:n=10
#[0,1,8,27...........1000]

n=int(input("enter the number"))
list=[]
for i in range(n+1):
    list.append(i*3)
print(list)


