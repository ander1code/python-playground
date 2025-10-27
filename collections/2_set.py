s1 = {1, 2, 3}
s2 = {3, 4, 5}
union = s1 | s2
print(union)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.union(s2)
print(s1)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
intersection = s1 & s2 # mostra apenas o que é comum ambos
print(intersection)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.intersection(s2) # mostra apenas o que é comum ambos
print(s1)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
difference  = s1 - s2 # mostra apenas o que ta em s1, e os que repetem e estão presente em s2.
print(difference)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.difference(s2) # mostra apenas o que ta em s1, e os que repetem e estão presente em s2.
print(s1)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
symmetric_difference  = s1 ^ s2 # elimina os que estão presentes em ambos.
print(symmetric_difference)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.symmetric_difference(s2) # elimina os que estão presentes em ambos.
print(symmetric_difference)