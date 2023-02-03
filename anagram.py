#write a progam to check whether the given input is satisfing the condition of anagram
#input1:listen
#input2:silent
#output:true
#test case 2-2
#i1=space
#i2=racer
#output:false

str1=input("enter a word")
str2=input("enter a word")
n=len(str1)
m=len(str2)
sortstr1=sorted(str1)
sortstr2=sorted(str2)
if n==m:
    if sortstr1==sortstr2:
        print("anagram")
    else:
        print("not a anagram")
else:
    print("length is not matching")