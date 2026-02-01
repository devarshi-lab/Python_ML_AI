addition = lambda a,b :a + b
subtraction = lambda a,b :a - b

no1 = 0
no2 = 0
ans = 0

no1 = int(input("Enter first number : "))   # 11
no2 = int(input("Enter second number : "))  # 10

ans = addition(no1,no2)             # ans = no1 + no2

print("Addition is : " , ans)

ans = subtraction(no1,no2)          # ans = no1 - no2
print("Subtraction is : " , ans)
