#set - a collection of item that cannot have duplicate items

s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(150)
s.add(3)
s.add(4)
s.add(10)
s.add(2)
s.add(6)
s.add(7)
s.add(8)
s.add(9)
s.add(0)
s.add(11)
s.add(15)
s.add(123)
s.add(13)
s.add(12)
s.add(120)
s.add(14)
s.add(120)
print(s)

#Set is an unsorted collection, but it gets some sorting a little. 
#Use "sorted" to make ensure it is sorted properly
print(sorted(s))