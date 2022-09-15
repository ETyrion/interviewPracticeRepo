read_names = open('wizardingWorld.txt', 'r')

names_list= read_names.readlines()
name_count={}
print(names_list)
for i in range(len(names_list)):
    firstname = names_list[i].split()
    print(firstname)
    if firstname[1] not in name_count.keys():
        name_count[firstname[1]] = 1
    else:
        name_count[firstname[1]] = name_count[firstname[1]]+1

print(name_count)

read_names.close()
