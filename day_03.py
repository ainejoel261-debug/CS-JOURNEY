for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

count = 1
while count <= 5:
    print(count)
    count = count + 1

#=====================================================================================

total = 0
for number in range(1, 6):
    total = total + number
print(total)

number = int(input("Enter a number: "))
for i in range(1, (number +1)):
    print(i)

number = int(input("Enter a number less than 3: "))
while number <= 10:
    number += 1
print("The sum is:" ,number)

number = int(input("Enter a number: "))
if number%2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
