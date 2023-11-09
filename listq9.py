number=[]
square=[]
cube=[]
start=int(input("ENTER THE START OF THE LIST :"))
stop=int(input("ENTER THE STOP OF THE LIST :"))
for i in range(start,stop+1):
    number.append(i)
    square.append(i**2)
    cube.append(i**3)
print("LIST IS         :",number)
print("SQUARE LIST IS  :",square)
print("CUBE LIST IS    :",cube)    