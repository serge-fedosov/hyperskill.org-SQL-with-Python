# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

new_groups = dict.fromkeys(groups, None)
n = int(input())
for key in range(n):
    new_groups[groups[key]] = int(input())

print(new_groups)
