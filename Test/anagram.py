def isAnagram(a, b):
    # code here
    a = sorted(a)
    b = sorted(b)
    if a == b:
        print("YES")
    else:
        print("NO")

isAnagram('bdc', 'bcd')
