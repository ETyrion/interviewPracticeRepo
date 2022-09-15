# t1 = (1,2,3)
# t2 = (4,5)
#
# t1 = t1+t2
# print(t1)

s1 = "ABAFGyyG"

s2= "" +s1[0]

for i in range(1, len(s1)):
    if (s1[i] not in s2):
        s2 = s2+s1[i]
print(s2)