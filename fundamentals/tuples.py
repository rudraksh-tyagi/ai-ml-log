# tuple -> A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

coordinates = (10, 20)
print(coordinates[0])  # prints 10
print(coordinates[1])  # prints 20
# coordinates[1] = 24  # This will raise an error since tuples are unchangeable
print(tuple.count(coordinates, 10))  # counts occurrences of 10 in the tuple
print(tuple.index(coordinates, 20))  # returns the index of 20 in the tuple