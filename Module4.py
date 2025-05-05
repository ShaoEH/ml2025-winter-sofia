number = int(input("Please enter how many integer you want to input: "))
inputs = []
for i in range(number):
    value = int(input("Please enter the number one by one: "))
    inputs.append(value)

target = int(input("Please enter the target value you want to look at: "))

if target in inputs:
    index = inputs.index(target) + 1
    print(index)
else:
    print(-1)