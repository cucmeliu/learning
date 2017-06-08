
#8-1 slice
L = range(1, 101)

print L[:10]
print L[2::3]
print L[4:51:5]

#8-2 invert slice
L = range(1, 101)
print L[-10:]
print L[-46::5]

#8-3 slice string
def firstCharUpper(s):
return s[0:1].upper()+s[1:]

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')


