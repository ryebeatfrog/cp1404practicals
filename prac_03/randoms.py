'''
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

Write code, not a comment, to produce a random number between 1 and 100 inclusive.



# 14, 19, 16
# 5,7, 7
# 3.73490, 5.16331, 2.934639

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

1. the smallest number would have been 5 and the highest, 20
2. the smallest would be 1 and the largest, 7
3. the smallest, 2.5 and the largest 5.5

'''

import random
print(random.randrange(1,101))
# for i in range(1,101):
#     print(i)
# print()


