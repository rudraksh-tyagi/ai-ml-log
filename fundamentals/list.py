l = [1, 2, 3, 4, 5]
print(l[0] + l[1] + l[2] + l[3] + l[4])  # list indexing
print(l[0:5])  # list slicing
print(l[0:5:2])  # list slicing with step
print(l[-1])  # last element
print(l)
print(l.index(3))  # index of element
l.append(6)  # add element to the end of the list
l.insert(5, 0)  # add element at specific index
print(l)
l.remove(3)  # remove element from the list
print(l.count(2))  # count occurrences of an element
print(l.pop(1))  # delete element at specific index and return it
