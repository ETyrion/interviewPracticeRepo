#ip_list = {"ram","rrr","nitin","naman","dgjdgsiuiu","uuu", "malayalam"}
ip_list = ["ram","rrr","nitin","naman","dgjdgsiuiu","uuu", "malayalam"]
input_list = ip_list
pal_list = dict()

for i in range(len(input_list)):
    ip_word = input_list[i]
    if ip_word == ip_word[::-1]:
        len_word = len(ip_word)
        pal_list[ip_word] = len_word

pal_len = max(pal_list.values())

print(pal_list)

for k, v in pal_list.items():
    if v ==pal_len:
        print(k)