'''
Loops
'''

#test)
# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()

# a) 1 - 100 in 10s
# for i in range(0, 110, 10):
#     print(i, end=' ')
# print()

# b) 20 - 1 backwards
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()

#c) number of stars
# number_of_stars = int(input("How Many Stars would you like?: "))
# for i in range(number_of_stars):
#     print("*", end=' ')
# print()

# d) number of lines
number_of_lines = int(input("How Many Lines would you like?: "))
for i in range(1, 10, number_of_lines):
    print("*", end=' ')
print()