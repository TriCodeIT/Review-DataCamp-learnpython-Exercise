#To find out which members attended both events, you may use the "intersection" method:
#To find out which members attended only one of the events, use the "symmetric_difference" method:
#To find out which members attended only one event and not the other, use the "difference" method:
#To receive a list of all participants, use the "union" method:

#Exercise
#In the exercise below, use the given lists to print out a set containing all the participants from event A which did not attend event B.

a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

A=set(a)
B=set(b)

print(A.difference(B))