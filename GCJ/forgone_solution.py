def getSum(i):
    number = int(input())
    if '4' not in str(number):
        return number
    else:
        curr_number = number
        curr = 1
        locations = []
        while curr_number:
            digit = curr_number % 10
            curr_number //= 10
            if digit == 4:
                locations.append(curr)
            curr *= 10
        operand = sum([n * 2 for n in locations])
        newNumber = number - operand
        return 'Case #{}: {} {}'.format(i, operand, newNumber)


t = int(input())
results = []
for i in range(1, t + 1):
    results.append(getSum(i))

for result in results:
    print(result)
