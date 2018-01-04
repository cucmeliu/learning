#7-2 function
L = []
i=1
while i<=100:
L.append(i*i)
i=i+1

print sum(L)


#7-3 def
def square_of_sum(L):
rst = 0
for l in L:
rst = rst+l*l
return rst

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])


#7-4 return mul var
import math

def quadratic_equation(a, b, c):
t = math.sqrt(b * b - 4 * a * c)
return (-b + t) / (2 * a),( -b - t )/ (2 * a)

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)


#7-5 recursion
def move(n, a, b, c):
if n ==1:
print a, '-->', c
return
move(n-1, a, c, b)
print a, '-->', c
move(n-1, b, a, c)

move(4, 'A', 'B', 'C')


#7-6 default param
def greet(who='world'):
print 'Hello, ', who, '.'

greet()
greet('Bart')


#7-7 *args
def average(*args):
sum=0.0
if len(args) == 0:
return sum
for arg in args:
sum=sum+arg
return sum / len(args)


print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)








