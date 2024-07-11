from fake_math import divide as wrong
from true_math import divide as right

result1 = wrong(69, 3)
result2 = wrong(3, 0)
result3 = right(49, 7)
result4 = right(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)