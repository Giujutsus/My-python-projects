values = []
currentNo = 0
even = []
odd = []

total = int(input("How many numbers do you want to type in? "))
while total < 0:
    total = int(input("That is an invalid value. How many numbers do you want to type in? "))
else:
    for i in range(0, total):
        currentNo = int(input("Enter your number here: "))
        values.append(currentNo)

for i in range(len(values)):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
print("The even numbers in this list are:  ", even)
print("The odd numbers in this list are: ", odd)