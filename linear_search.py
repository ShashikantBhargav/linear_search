lst = [1,4,3,5,6,7,8,5]
key = 5
for i in range(len(lst)):
    if key == lst[i]:
        print(key, "is at index of ", i)
        break
