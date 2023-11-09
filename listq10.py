data=[12,23,56,89,81,20,23,89,20,85]
print(data)
print(len(data))
for i in data:
    if i%2==0:
        data.remove(i)
print(data)
print(len(data))     