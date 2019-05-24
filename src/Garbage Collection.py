__about__ = """ 
            
                Garbage collection in Python. 
            
            """


a = []
a.append(a) # Self reference.

a = 100        # Create object <100>
b = a          # Increase ref. count  of <100>
c = [b]        # Increase ref. count  of <100>
del a          # Decrease ref. count  of <100>
b = 80         # Decrease ref. count  of <100>
c[0] = -1      # Decrease ref. count  of <100>

