# Import specified objects in the module
# with alternate names.
from mod import num as my_num
from mod import hello as my_hello


# Access objects in the module through
# the alternate names.
print(my_num)
my_hello()