__about__ = """ Shallow and Deep Copy """


"""

Assignment statements in Python do not copy objects, 
they create bindings between a target and an object.

"""
from collections import OrderedDict
import copy

data = [1,2,3,4,[5,6,7,8],9]

data1 = copy.copy(data)

data2 = copy.deepcopy(data)

"""

Will not work for these cases.

"""

mydata = [1,2,3,4,5,6,7]

mydata1 = copy.copy(mydata)
mydata2 = copy.deepcopy(mydata)

mydata1[0] = 100

data1[4][3] = 10
data2[4][3] = 11
print(data)
print(data1)
print(data2)

print(mydata)
print(mydata1)
print(mydata2)

