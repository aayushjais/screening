def add(a,b):
   return a+b

def subtract(a,b):
   return a-b


def multiply(a,b):
   return a*b

def divide(a,b):
   return a/b

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

 
choice = str(input("Enter choice(1/2/3/4): "))

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if choice == '1':
   print(add(x,y))

elif choice == '2':
   print(subtract(x,y))

elif choice == '3':
   print(multiply(x,y)) 

elif choice == '4':
   print(divide(x,y))
else:
   print("Invalid input")
