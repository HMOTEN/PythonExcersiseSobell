#!/usr/bin/python

originalList = ['a','b','c','d']
print 'The original list is: '
print originalList
copyList = list(originalList)
copyList[1] = 'z'
print copyList
print 'Notice how the original list did not change even though we changed copy'
print originalList
