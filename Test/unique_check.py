S = "uryityrtyre"
us= ""

for i in S:
    if i not in us:
        us = us+i
    else:
        continue
print(us)