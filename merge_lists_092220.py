#!/usr/bin/python

class total():
  def __init__(self, g, h):
    self.g = g
    self.h = h

  def reversethem(self):
    print('After reverse two numbers becomes ' + str(self.h) + ' then ' + str(self.g) + ' done ')

# prompt user for nubmer

d = raw_input('Enter first number: ')
e = raw_input('Enter second number: ')
t1 = total(d, e)
t1.reversethem()

a = ['a', 'b', 'c']
b = ['d', 'e', 'f']

# merge two list

for c in b:
  a.append(c)

print(a)




