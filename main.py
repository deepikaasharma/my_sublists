"""Use slicing to create a list containing three sublists according to the following specifications:

    The first five elements from the original list
    The last five elements from the original list
    The middle five elements from the original list

Note: The resulting sublists should be assigned to the variable my_sublists in the order they are described above.
"""

my_list = list(range(-100, 101))

# Modify the code below according to the prompt
# Sublists

# print(len(my_list))
# sublist_1 = list(range(my_list[0], my_list[5]))
sublist_1 = my_list[0:5]

sublist_2 = my_list[196:201]

sublist_3 = my_list[98:103]

# lastfour_last = list(range(my_list[-5], my_list[-1]))

# sublist_2 = (lastfour_last[0],lastfour_last[1],lastfour_last[2],lastfour_last[3], my_list[-1])


# print(sublist_3)

# Collection of sublists
my_sublists = [sublist_1, sublist_2, sublist_3]

# print(my_sublists)

