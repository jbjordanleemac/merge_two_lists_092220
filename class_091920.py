#!/usr/bin/python

class day():
  happyday = 'Yes Happy Day Everyday, Still alive with God\'s mercy !!!'

  def __init__(self, whatday, dowhat):
    self.whatday = whatday
    self.dowhat = dowhat

# print classa variable
d1 = day('Same Sat', 'Still Working with Joy !!!')
print(d1.happyday)

d2 = day('Sat', 'Working Day')
print(d2.whatday) 

class day2(day):
  pass

d3 = day('Sat again', 'Standby Working Still !!!')
print(d3.dowhat)

# string is actually a list 

string1 = 'this is a string'
print(string1[1])

string2 = ' second string '

total = string1 + string2
print(total)

whichday = 'Sat'

if whichday == 'Fri':
  print('It is Fri !!!')
else:
  print('Not Fri !!!')

thisdict = {
  'Mon': 'One',
  'Tue': 'Two',
  'Wed': 'Three'
}

for a in thisdict:
  print(a)

goodday = "Today is a great day! Still alive!"
# This is how I add extra line in between
print("\n")
print(goodday)

goodday1 = goodday.split()
print(goodday1)

goodday2 = goodday.split('!')
print(goodday2)

goodday3 = goodday.strip()
print(goodday3)

goodday4 = goodday.upper()
print(goodday4)
