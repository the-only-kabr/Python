my_tuple_1 = ((1, 2), (34, 23), (2, 234), (56, 7))
# my_tuple_2 = (35,78,56)
# my_tuple_3 = (23,34,567,67,34,23,64)
# my_tuple_4 = ((1,2,35,78,56),(34,23,35,78,56),(2, 234,35,78,56), (56,7,35,78,56))
my_dict = dict(my_tuple_1)

# a,b,c = my_tuple_2
# print('a=', a, 'b=', b, 'c=', c)

# a,b,*c = my_tuple_1
# print('a=', a, 'b=', b, 'c=', c)

# a,*b,c = my_tuple_3
# print('a=', a, 'b=', b, 'c=', c)

# for i,j,z,w,t in my_tuple_4:
#     print(i,j,z,w,t)
print(my_dict)
for i in my_dict:
    print(i)

print(my_dict.keys())
for i in my_dict.keys():
    print(i)

print(my_dict.values())
for i in my_dict.values():
    print(i)

print(my_dict.items())
for key, value in my_dict.items():
    print(key, '-', value)

for key, value in sorted(my_dict.items()):
    print(key, '-', value)

print(sorted(my_dict))
print(sorted(my_dict.values()))
print(sorted(my_dict.items()))
