list1 = [1, 2, 3, 4, 5, 6]
print("First list is:", list1)
print(len(list1))
list2 = [2, 4, 6, 8, 10, 12]
print("Second list is:", list2)
print(len(list1))
newList = []
newList.extend(list1)
for element in list2:
    if element not in newList:
        newList.append(element)
print("Union of the lists is:", newList)
print(len(newList))