def fact(num):
    if num <= 1:
        return 1
    else:
        while num >1:

            fact_num = num*fact(num-1)
            return fact_num

print(fact(9))