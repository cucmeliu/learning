#6-1 dict
d = {

'Adam': 95,
'Lisa': 85,
'Bart': 59,
'Paul': 75
}

#6-2 access dict
d = {
'Adam': 95,
'Lisa': 85,
'Bart': 59
}
print 'Adam: ', d.get('Adam')
print 'Lisa: ', d.get('Lisa')
print 'Bart: ', d.get('Bart')

#ch6-3 -*- coding: utf-8 -*-
d = {
95: 'Adam',
85: 'Lisa',
59: 'Bart'
}

#6-4 update dict 
d = {
95: 'Adam',
85: 'Lisa',
59: 'Bart'
}
d[72]='Paul'


#6-5 accross dict
d = {
'Adam': 95,
'Lisa': 85,
'Bart': 59
}
for key in d:
print key, ': ', d.get(key)

#6-6 set
s = set(['Adam', 'Lisa', 'Bart', 'Paul'])


#6-7 access set
s = set(['adam','bart'])
print 'adam' in s
print 'bart' in s


#6-8 character of set 
months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
print 'x1: ok'
else:
print 'x1: error'

if x2 in months:
print 'x2: ok'
else:
print 'x2: error'

#6-9 accross set
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
print x[0],':',x[1]

#6-10 update set
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for l in L:
if l in s:
s.remove(l)
else:
s.add(l)
print s




