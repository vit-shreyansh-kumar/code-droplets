__about__ = """
            Test Garbage Collection.
            """

import ctypes


class PyObject(ctypes.Structure):

    _fields_ = [("refcnt",ctypes.c_long)]


class GaandObject(ctypes.Structure):

    _fields_ = [
        ("chut",ctypes.c_long)
    ]

# a = 100        # Create object <100>
# b = a          # Increase ref. count  of <100>
# c = [b]        # Increase ref. count  of <100>
# del a          # Decrease ref. count  of <100>
# b = 80         # Decrease ref. count  of <100>
# c[0] = -1      # Decrease ref. count  of <100>

obj_address = id(100)
print(PyObject)
print(GaandObject.from_address(obj_address).chut) #9 - by default ref count
a = 100
obj_address =  id(a)
print(PyObject.from_address(obj_address).refcnt) #10 - assignment increases ref count
b = a
print(PyObject.from_address(obj_address).refcnt) #11 - assignment increases ref count
c = [b]
print(PyObject.from_address(obj_address).refcnt) #12 - placing in container increases ref count
del a
print(PyObject.from_address(obj_address).refcnt) #11 - deleting with del decreases ref count
b = 80
print(PyObject.from_address(obj_address).refcnt) #10 - re-assignment decreases ref count
c[0] = -1
print(PyObject.from_address(obj_address).refcnt) #9 - re-assignment decreases ref count
