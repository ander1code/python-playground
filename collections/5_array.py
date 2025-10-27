import array

array1 = array.array("i", [5,6,7,4,3])
print(array1)
bytes = array1.tobytes()
print(bytes)

array2 = array.array("i")
array2.frombytes(bytes)
print(array2)
array2.byteswap()
print(array2)

# -------------------------

# array
    
import array

my_array = array.array("i", [1,2,3,4,5,6,7,8,9,0])
print(my_array)
for k,v in enumerate(my_array):
    print(f"[{k}]={v}")


import array

array1 = array.array("i", [5,6,7,4,3])
print(array1)
bytes = array1.tobytes()
print(bytes)

array2 = array.array("i")
array2.frombytes(bytes)
print(array2)
array2.byteswap()
print(array2)


