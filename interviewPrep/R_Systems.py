# import math
#
#
# def reverse_integer(ip_int):
#
#
#     rem = 0
#     rev_int = 0
#
#     if ip_int ==0:
#         return 0
#
#     elif ip_int > 0:
#         positive_val = ip_int
#         while (positive_val > 0):
#             rem = positive_val % 10
#             rev_int = rev_int * 10 + rem
#             positive_val = positive_val // 10
#     else:
#         positive_val = abs(ip_int)
#         while (positive_val > 0):
#             rem = positive_val % 10
#             rev_int = rev_int * 10 + rem
#             positive_val = positive_val // 10
#         rev_int = -rev_int
#
#
#     return rev_int
#
# rev = reverse_integer(-4422)
# print(rev)

file_path = 'log_file.txt'

def read_log_file(file_path):
    with open(file_path) as log_file:
        file_data = log_file.readlines()
        for i in file_data:
            p_id = i.split(' ')[0]
            p_status = i.split(' ')[1]

            p_id_status_dict = dict()

            p_id_status_dict[p_id] = p_id_status_dict[p_id]+p_status


    print(p_id_status_dict)
    failed_ids = []
    for k,v in p_id_status_dict.items():
        if v[:5] !='begin' or v[len(v)-4:] != 'end':
            failed_ids.append(k)
    print(failed_ids)

read_log_file(file_path)