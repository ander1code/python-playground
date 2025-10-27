# DEFAULT_DICT:

from collections import defaultdict 

colors = [('yellow',1),('red',1),('blue',2),('green',5),('red',2)]
print(colors)

d = defaultdict(list)

for k,v in colors:
    d[k].append(v)

print(d)

# ------------------

from collections import defaultdict
cont = defaultdict(int)
cont["item_01"] += 1
cont["item_02"] += 2
cont["item_03"] += 3
print(cont)

lists = defaultdict(list)
lists[0].append("Anderson")
lists[0].append("Paula")
lists[1].append("Anne")
print(lists)
print(lists[0])
for i in lists[0]:
    print(i)

lists[0].append("Rita")

for k,v in lists.items():
    print(f"[{k}] = {v}")


