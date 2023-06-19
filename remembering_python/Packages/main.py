import mypackage.module1 as m1
import mypackage.module2 as m2
from mypackage.subpackage.module3 import people


m1.greet("Mikhail")
m2.depart("Mikhail")

for i in people:
    print(i)
