#Part 1

#priority levels = (a-z 1-26) (A-Z 27-52)
priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
rdict = dict([(x[1], x[0]) for x in enumerate(priority)])

sum = 0

#open and iterate through the bag to create a list of lines
with open('bag.txt') as all_bags:
  for bag in all_bags:
    bag = bag.strip()

    #divide the lines in half (Two compartments)
    size = (int)(len(bag) // 2)
    x = bag[:size]
    y = bag[size:]

    #first half set x, second half set y
    comp1 = set(x)
    comp2 = set(y)

    #store duplicate terms
    c = list(comp1.intersection(comp2))

    #add up their priority level
    for char in c:
      sum += rdict[char] + 1

print('The sum of duplicate compartment items:', sum)


#Part 2
rucksacks = []
sum_of_badges = 0

with open('bag.txt') as all_bags:
  for bag in all_bags:
    bag = bag.strip()
    rucksacks.append(bag)
    
for i in range(0, len(rucksacks), 3):
  
  x1 = set(rucksacks[i])
  x2 = set(rucksacks[i+1])
  x3 = set(rucksacks[i+2])

  y1 = x1.intersection(x2)
  y2 = y1.intersection(x3)

  badges = list(y2)

  for badge in badges:
    sum_of_badges += rdict[badge] + 1
    
print('The sum of elf badges:',sum_of_badges)