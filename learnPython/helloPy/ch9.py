#9-1 iterator
for i in range(1, 101):
if i % 7 ==0:
print i

#9-2 index iter
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
print index+1, '-', name

#9-3 iter dict
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for v in d.values():
sum=sum+v
print sum / len(d)


#9-4 iter key-value
sum = 0.0
for k, v in d.items():
sum = sum + v
print k, ':', v
print 'average', ':', sum / len(d)










