# DEQUE:

from collections import deque

vetor = ['r','u','w','q','e','v','q','r','r']
d = deque(vetor)
d.append("Python 3") # final
d.appendleft("Python 2.7") # initial
print(d)

for el in d:
    print(el, end=", ")

# --------------
    
# deque

from collections import deque

vetor = ['r','u','w','q','e','v','q','r','r']
d = deque(vetor)
d.append("jsdhjdashd")
d.appendleft("append_left_item")
print(d)



