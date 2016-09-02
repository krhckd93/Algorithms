a = [int(x) for x in input().split(',')]
print(a)

for i in range(0, len(a)):
    index = a[i]
    j = i
    while j > 0 and a[j-1] > index:
        a[j] = a[j-1]
        j -= 1
        print(a)
    a[j] = index
print("a is:", a)
