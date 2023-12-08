def Sum(n):
    s = 0
    while n != 0:
        s += n % 10
        n = n // 10 
    return s

def Quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = [data[0]]
        left = []
        right = []
        for i in data[1:]:
            if i == data[0]:
                pivot.append(i)
            elif (Sum(i) < Sum(pivot[0])) or (Sum(i) == Sum(pivot[0]) and i < pivot[0]):
                left.append(i)
            else:
                right.append(i)
        return Quick_sort(left) + pivot + Quick_sort(right)
    
lst = [int(i) for i in input().split()]
print(Quick_sort(lst))