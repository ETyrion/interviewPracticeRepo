
class count_object():
    count =0
    def __init__(self):
        count_object.count = count_object.count+1

obj1 = count_object()
obj2 = count_object()
obj3 = count_object()
print('Total objects created are: ' , count_object.count)


list1= [10,5,18,19,25,25]

sum_list = sum(list1)
print(sum_list)

def return_second_highest(num_list):
    len_list = len(num_list)
    for i in range(len_list):
        for j in range(i+1, len_list):
            if num_list[i] < num_list[j]:
                temp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = temp
    print(num_list)
    return num_list[1]

second_highest = return_second_highest(list1)
print(second_highest)

