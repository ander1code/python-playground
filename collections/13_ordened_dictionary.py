
# ORDERED_DICT:

from collections import OrderedDict

d = OrderedDict()
d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8] = 'A','n','d','e','r','s','o','n'
print(d.keys())
print(d.values())
print(d.items())
print(f"{d.get(6)}{d.get(7)}{d.get(8)}")
