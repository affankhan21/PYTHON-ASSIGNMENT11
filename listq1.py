data1=[34,89,78,23,765,93,68,98,55,82,66,34]
evenl=[]
oddl=[]
for i in data1:
    if (i%2==0):
        evenl.append(i)
    else:
        oddl.append(i)
print("ORIGINAL LIST :",data1)
print(len(data1))
print("EVEN LIST IS  :",evenl)
print(len(evenl))
print("ODD LIST IS :",oddl)
print(len(oddl))
