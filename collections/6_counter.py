# COUNTER:

from collections import Counter

# imprime nome porem, colocando o indice em cada letra.
c = Counter('Anderson')
print(c) # Counter({'n': 2, 'A': 1, 'd': 1, 'e': 1, 'r': 1, 's': 1, 'o': 1})

c = Counter({'red':4,'blue':2,'red':4})
print(c)

c = Counter(cats=5,dogs=7)
print(c)

nums = [4,2,6,7,8,1,3,4,6,8,2,4,5,6,7,8,9,3,9,2,3,5,6,9,8,3,0,1,2,4,5,7,0]
c = Counter(nums)
print(c) # Counter({4: 4, 2: 4, 6: 4, 8: 4, 3: 4, 7: 3, 5: 3, 9: 3, 1: 2, 0: 2})

print(Counter("Anderson").most_common())

print(c.elements())

# ------------

# counter:

from collections import Counter
my_counter = Counter("Anderson")
print(my_counter)
print(my_counter.most_common())

from collections import OrderedDict

o = OrderedDict([
    (1, "Zenny"),
    (2, "Carmen"),
    (3, "Yasmin"),
    (4, "Wiiliam"),
    (5, "Anderson"),
    (6, "Bernard"),
    (7, "Anne")
])

print(o)


