import sys

'''values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)'''

print("Enter a comma separated array")
a = [int(x) for x in input().split(',')]

for i in range(len(a)-1, 0, -1):
    for j in range(1, i+1):
        if a[j] < a[j-1]:
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp
        print(a)
