# input_string = "today is the good day"


def uniq_op(ip_str):
    uniq_str = ''

    for i in range(len(ip_str)):
        if (ip_str[i] not in uniq_str):
            uniq_str = uniq_str + ip_str[i]
        else:
            pass
    return uniq_str


input_string = "today is the good day"

output_str = uniq_op(input_string)
print(output_str)