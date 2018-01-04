#5-1 if
score = 75
if score>=60:
print 'passed'

#5-2 if-else
score = 55
if score>=60:
print 'passed'
else:
print 'failed'

#5-3 if-elif-else
score = 85

if score>=90:
print 'excellent'
elif score>=80:
print 'good'
elif score>=60:
print 'passed'
else:
print 'failed'

#5-4 for
L = [75, 92, 59, 68]
sum = 0.0
for score in L:
    sum=sum+score
print sum / 4.0

#5-5 while
sum = 0
x = 1
while x<=100:
    sum=sum+x
    x=x+2
print sum

#5-6 break
sum = 0
x = 1
n = 1
while True:
    sum=sum+x
    x=2*x
    n=n+1
    if n>20:
        break
print sum

#5-7 continue
sum = 0
x = 0
while True:
x = x + 1
if x > 100:
break
if x%2 ==0:
continue
sum=sum+x
print sum

#5-8 mul-loop
for x in [ 1, 2, 3, 4, 5, 6, 7, 8, 9]:
for y in [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]:
if x<y:
print x,y




