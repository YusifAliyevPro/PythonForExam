a = [3, 4, 5, 6, 7, 8, 2, 9, 1, 12]
average = sum(a)/len(a)

for i in a:
    if i > average:
        print(i)

# Output:
# 6
# 7
# 8
# 9
# 12
