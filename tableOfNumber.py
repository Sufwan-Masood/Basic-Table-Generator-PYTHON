
#table of any number given by the user
print("This program prints table of your given number from 1 to 10.")

number=int(input("Enter the number: "))

for i in range(1,11):
  
  result=number * i
  print(f"{number}x{i}={result}")


