a = [int(x) for x in input("Enter comma separated list:").split(',')]


def merge(a, l, r):
    j = 0
    k = 0
    i = 0
    la = len(a)
    ll = len(l)
    lr = len(r)

    while j < ll and k < lr:
        if l[j] <= r[k]:
            a[i] = l[j]
            i += 1
            j += 1
        elif l[j] > r[k]:
            a[i] = r[k]
            k += 1
            i += 1
        else:
            print("Error! i:", i, " j:", j, " k:", k)

    if j < ll:
        while j < ll:
            a[i] = l[j]
            i += 1
            j += 1
    elif k < lr:
        while k < lr:
            a[i] = r[k]
            i += 1
            k += 1

    return a


def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        la = len(a)
        l = a[0:int(la/2)]
        r = a[int(la/2):]
        l = merge_sort(l)
        r = merge_sort(r)
        a = merge(a, l, r)
    return a

a = merge_sort(a)
print(a)
