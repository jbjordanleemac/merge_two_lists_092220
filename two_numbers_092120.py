#!/usr/bin/python

class total():
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def plus(self):
    result = self.first + self.second
    return result

t1 = total(3, 5)
print(t1.plus())

# how to reverse the numbers

firstnumber = raw_input('Please enter the first number: ')
secondnumber = raw_input('Please enter the second number: ')

class twonumbers():
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def reversenumbers(self):
    print('Here you go after the reverse: ' + str(self.b) + ' then ' + str(self.a) + ' looks good ')

t1 = twonumbers(firstnumber, secondnumber)
print('After the number reverse: ')
t1.reversenumbers()


thislist = ['a', 'b', 'c', 'd']

d = raw_input(' Which location of the node you wish to pop out: Enter the number ')
thislist.pop(int(d))

print('After pop up ' + d + ' element Now list becomes ') 

for c in thislist:
  print(c)

# how to remove the duplicated node from the list

e = [0, 0, 1, 1, 1]

g = len(e)
h = 0

while h < g:
  if e[h] == e[h + 1]:
    e.pop(h+1)
  h += 1

print(e)
      


