data2=[34,89,78,23,765,93,68,98,55,82,66,34]
data3=[56,89,90,23,55,6,78,90,22,65,2,3,]

finallist = []

for i in data2:

  if i in data3:

      finallist.append(i)

print("INTERSECTION OF LIST ",finallist)