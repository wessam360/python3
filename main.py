# in python we can assign bolean to only integer 
a:int
a=False
# a="Fasle"
# a=True
#b print(a)

# automatic type casting (explicit)
b=4
# b="ok"

# 
# x it will give error to assign. not automatically take any like typescript
# x:int it will not give error
from typing import Any
c:Any
# c.to() type checking stops
#y print(type(c)) #  error: c not defined 

d:Any=67 
#o print(type(d))  <class `int`>


e="ok"
e=12
print(type(c)) #p<class `str`>
print(id(c)) #momoery address
print(dir(c)) # method and attributes of defined class



