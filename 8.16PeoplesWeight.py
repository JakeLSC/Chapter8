weights = [ ]

for i in range(4):
    weight = float(input('Enter weight {}:\n'.format(i + 1)))
    weights.append(weight)

print('Weights: {}\n'.format(weights))

#2 & 3
print('Average weight: {:.2f}'.format(sum(weights) / 4))
print('Max weight: {:.2f}\n'.format(max(weights)))

#4
userPick = int(input('Enter a list index (1 - 4):\n'))
weightPick = weights[userPick - 1]
print('Weight in pounds: {:.2f}'.format(weightPick))
print('Weight in kilograms: {:.2f}\n'.format(weightPick / 2.2))

#5 sort the list
weights.sort()
print('Sorted list: {}'.format(weights))
