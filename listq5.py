l=[]
num=int(input('ENTER NUMBER OF ELEMENT :'))
for i in range(1,num+1):
    n=input("ENTER ELEMENT :")
    l.append(n)
print("ORIGINAL LIST IS        :",l)
l.sort(key=len)
print("AFTER SORTING  LIST IS  :",l)    