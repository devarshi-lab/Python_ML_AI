class arithmatic:

    def addition(self,no1,no2):
        return no1 + no2

    def subtraction(self,no1,no2):
        return no1 - no2

no1 = 0
no2 = 0
ans = 0

no1 = int(input("Enter first number : "))
no2 = int(input("Enter second number : "))

obj = arithmatic()

ans = obj.addition(no1,no2)

print("Addition is : " , ans)

ans = obj.subtraction(no1,no2)
print("Subtraction is : " , ans)