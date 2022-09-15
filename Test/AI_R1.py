# Same number of unique characters
# Same frequency of characters

# SILENT, LISTEN

def is_anagram(str1='', str2=''):
    dict_1 = dict()
    dict_2 = dict()
    count=0

    sort_str1 = sorted(str1)
    sort_str2 = sorted(str2)
    if len(str1) != len(str2):
        print("Length is different")
        return False

    for i in range(len(str1)):
        char_i = str1[i]
        if char_i in dict_1.keys():
            dict_1[char_i] = dict_1[char_i]+1
        else:
            dict_1[char_i]= 1

    for j in range(len(str2)):
        char_j = str2[j]
        if char_j in dict_2.keys():
            dict_2[char_j] = dict_2[char_j]+1
        else:
            dict_2[char_j]= 1

    print(dict_1 , dict_2)

    if dict_1 == dict_2:
        print("Valid Anagram")
    else:
        print("Not")


is_anagram(str1='SILENTE', str2='LISTEN')
