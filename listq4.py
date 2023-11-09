a=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS :"))
for i in range(1,n+1):
    num=int(input("ENTER  ELEMENT :"))
    a.append(num)
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
         if (a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp 
print("SECOND LARGEST ELEMENT IS ",a[n-2])              