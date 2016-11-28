#!/usr/bin/python

list = [1,2,3,4]
print list
print (map(lambda x:x*x, list))

print (map(lambda x: x%2==0, range(4,15)))
