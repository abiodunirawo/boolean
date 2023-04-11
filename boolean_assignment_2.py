#  Write a Python function that takes 10 lists and returns True if they have
# at least one common member in atleast two of the lists.

# FOR COMMON NUMBER 10 LISTS;

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]
list4 = [6, 7, 8, 9]
list5 = [7, 9, 10, 11]
list6 = [1, 3, 5, 7]
list7 = [2, 4, 6, 8]
list8 = [1, 5, 9, 13]
list9 = [2, 6, 10, 14]
list10 = [3, 7, 11, 15]

# identifying and comparing common elements in the lists

common_elements1 = set(list1).intersection(list2)
common_elements2 = set(list1).intersection(list3)
common_elements3 = set(list1).intersection(list4)
common_elements4 = set(list1).intersection(list5)
common_elements5 = set(list1).intersection(list6)
common_elements6 = set(list1).intersection(list7)
common_elements7 = set(list1).intersection(list8)
common_elements8 = set(list1).intersection(list9)
common_elements9 = set(list1).intersection(list10)

common_elements = ( common_elements1, common_elements2, common_elements3, common_elements4, common_elements5, common_elements6, common_elements7, common_elements8, common_elements9,)


print(common_elements)

if common_elements:
    print(True)
else:
    print(False)