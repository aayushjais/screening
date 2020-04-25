n=int(input("enter a no: "))

if n%2==0:
    for i in range(1,2*(n-1)):
        if i%2!=0:
            print(i,end=", ")
   
else:
    for i in range(1,2*n):
         if i%2!=0:
            print(i,end=", ")
