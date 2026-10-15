

# FILENAME = "name.txt"
# in_file = open(FILENAME, 'r')
# # out_file = open(FILENAME, 'w')
# read_name = in_file.readlines()
# print(read_name)
# # name = input("What is your name: ")
# # print({name}, file=out_file)
#

#
FILENAME = "numbers.txt"
text = FILENAME.strip()
in_file = open(FILENAME, 'r')
for line in in_file:
    print(line)
print()
# line1 = in_file.readlines(1)
# line2 = in_file.readlines(2)
# print(line1, line2)
# # sum = (line1 + line2)
# print(line1 * line2)

# with open("heroes.txt", "r") as heroes:
# hlist = heroes.read().splitlines()
# print(hlist)





